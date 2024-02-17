import inspect
import json
import logging
import textwrap
import traceback
import typing
from dataclasses import is_dataclass, fields
from datetime import datetime
from functools import wraps
from typing import Callable, Dict, Optional, List

from IPython.core.interactiveshell import InteractiveShell
from IPython.core.magic import Magics, magics_class, cell_magic, line_magic
from IPython.display import display, Markdown

from junon.llm_util import query_to_agent, StreamHandler
from junon.util import log_util, conversation_history_util
from junon.util.ai_config_util import save_default_parameters, load_default_parameters
from junon.util.conversation_history_util import Message
from junon.util.nb_util import create_argument_parser

logger = logging.getLogger(__name__)


class FunctionExecutor:
    """
    agentからの要求に応じて、各種関数(ツール)を実行する。
    コンストラクタに実行可能な関数のリストを渡しておくこと。
    ただし何れの関数も、@function_schemaデコレータで就職されている必要がある（それによって自動的にfunction定義に必要な情報を取得する）
    """

    def __init__(self, functions: List[callable]):
        self.functions = dict()
        for f in functions:
            if callable(f) and hasattr(f, 'schema'):
                self.functions[f.schema['name']] = f
            else:
                raise ValueError(f"{f} is not a schem-able function")

    def execute(self, function_name: str, arguments_json: str) -> Optional[Dict]:
        try:
            function = self.functions.get(function_name, None)
            if function is None:
                raise ValueError(f"function_name={function_name} is not found")
            sig = inspect.signature(function)
            sig_params = sig.parameters

            # 引数をデシリアライズ
            arguments = json.loads(arguments_json)
            parameters = dict()
            # dict等をdataclassに変換
            for param_name, param_value in arguments.items():
                sig_param = sig_params[param_name]
                py_type = sig_param.annotation
                parameters[param_name] = type_and_dict_to_value(py_type, param_value)

            return function(**parameters)
        except Exception as e:
            print(traceback.format_exc())
            return dict(error=str(e))

    def get_functions_definition(self) -> List[Dict]:
        return [f.schema for f in self.functions.values()]


# abstractにするとmagic_class関連のデコレータが機能しなくなる
class AssistantMagicBase(Magics):

    def __init__(self, shell: InteractiveShell, executor: FunctionExecutor):
        super().__init__(shell)

        # executorを保持（この後スグに使われる）
        self.executor = executor

        self.shell = shell

        # ログ初期化（実行ごとにディレクトリを分ける）
        log_util.init_for_wa('latest')

        # デフォルトパラメタロード
        self.default_parameters = load_default_parameters()

        # 会話履歴ロード
        self.messages = conversation_history_util.load(self.get_conversation_history_json_path())
        self.start_first_message()

    def system_message_on_init(self) -> str:
        """
        初回起動時のシステムメッセージを返す。
        :return:
        """
        raise NotImplementedError()

    def system_message_on_new_start(self) -> str:
        """
        新規プロジェクト開始時のシステムメッセージを返す。
        :return:
        """
        raise NotImplementedError()

    def system_message_on_continue(self) -> str:
        """
        既存プロジェクトの引継ぎ時のシステムメッセージを返す。
        :return:
        """
        raise NotImplementedError()

    def get_tool_executor(self) -> FunctionExecutor:
        """
        ツール実行用のFunctionExecutorを返す。
        :return:
        """
        raise NotImplementedError()

    def get_conversation_history_json_path(self) -> str:
        """
        会話履歴のJSONファイルパスを返す。
        :return:
        """
        raise NotImplementedError()

    def is_current_session_continued(self) -> bool:
        """
        現在のセッションが引継ぎ（会話履歴はないがその他のデータは残っている状態）であるかどうかを返す。
        :return:
        """
        raise NotImplementedError()

    def start_first_message(self):
        if not self.messages:
            first_system_prompt = self.system_message_on_init()
            self.messages.append(Message(
                timestamp=datetime.now().isoformat(),
                role='system',
                content=first_system_prompt
            ))

            # 言語に関する指示
            self.messages.append(Message(
                timestamp=datetime.now().isoformat(),
                role='system',
                content=f"This user-environment default language setting is "
                        f"{self.default_parameters['user_communication_language']}. "
                        f"Please use this language when communicating with user unless otherwise specified by user."
            ))

            if not self.is_current_session_continued():
                # 引継ぎではない＝新しいプロジェクトを開始した
                second_system_prompt = self.system_message_on_new_start()
                self.messages.append(Message(
                    timestamp=datetime.now().isoformat(),
                    role='system',
                    content=second_system_prompt
                ))
            else:
                # 引継ぎ
                second_system_prompt = self.system_message_on_continue()
                self.messages.append(Message(
                    timestamp=datetime.now().isoformat(),
                    role='system',
                    content=second_system_prompt
                ))

        else:
            # 会話履歴がある場合は、ユーザが作業を中断したことを通知する
            last_timestamp = self.messages[-1].timestamp
            self.messages.append(Message(
                timestamp=last_timestamp,
                role='system',
                content=f"{last_timestamp} : User interrupted work."
            ))
            current_timestamp = datetime.now().isoformat()
            self.messages.append(Message(
                timestamp=current_timestamp,
                role='system',
                content=f"{current_timestamp} : User is back to work."
            ))

        # エージェント実行
        self._do_agent(temperature=self.default_parameters['temperature'],
                       model=self.default_parameters['model'])

    def usage(self, line):
        guidance = textwrap.dedent("""
        ----------------------------------------
        ### How to Use
        
        ## Basic Usage:
        
        You can issue instructions to this assistant by writing `%%agent` followed by the instruction in a code block, and then executing the cell (`Shift+Enter`, etc). For example:
        
        ```
        %%agent
        I feel that Chapter XX is starting to deviate from the concept of this project.
        Please create a revision plan.
        ```

        ## Commands:
        
        Other commands include:
        - `%undo` : Delete the last input and output. 
        - `%redo` : Delete the last output and regenerate (with the same input as last time). 
        - `%history` : Display conversation history
        - `%reset_conversation_history` : Completely delete the conversation history
        - `%resume` : Continue the output without adding user instructions
        
        Executing commands with `-h`, like `%history -h` or `%reset_conversation_history -h`, will display help for each command.
        """)
        display(Markdown(guidance))

        # systemメッセージで表示したことを記録しておく。（ユーザから質問があったときにagentが対応できるようにするため）
        self.messages.append(Message(
            timestamp=datetime.now().isoformat(),
            role='system',
            content=f"User was shown the usage guidance.\n\n{guidance}"
        ))
        conversation_history_util.save(self.messages, self.get_conversation_history_json_path())

    def history(self, line):
        arguments_parser = create_argument_parser(
            prog='%history', line=line,
            description='Show conversation history.'
        )
        arguments_parser.add_argument(
            '-n', '--lines',
            type=int, default=5,
            help='Specify the number of rows to display (latest n). Default is 5 lines. Specify 0 to display everything.'
        )
        arguments = arguments_parser.get_arguments()
        if arguments is None:
            return

        if arguments.lines:
            target_messages = self.messages[-arguments.lines:]
        else:
            target_messages = self.messages

        sh = self.get_stream_handler_class()()
        # 会話履歴を表示
        for message in target_messages:
            sh.display_message(message)

        # トークン数を表示
        total_token_count = conversation_history_util.get_token_count(self.messages)
        print(f'Number of used tokens : {total_token_count:,} / 132,000')

    def reset_conversation_history(self, line):
        arguments_parser = create_argument_parser(
            prog='%reset_conversation_history',
            line=line,
            description='Permanently delete conversation history'
        )
        arguments_parser.add_argument('-y', '--yes',
                                      action='store_true', default=False,
                                      help='Flag to run without confirmation')
        arguments = arguments_parser.get_arguments()
        if arguments is None:
            return

        if not arguments.yes:
            print('Permanently delete conversation history. Is it OK? (y/n)')
            answer = input()
            if answer != 'y':
                print('Processing has been interrupted.')
                return

        # 会話履歴を削除
        self.messages = []
        conversation_history_util.save(self.messages, self.get_conversation_history_json_path())
        print('Conversation history has been deleted.')

        # 会話開始
        self.start_first_message()

    def __add_agent_params_to(self, arguments_parser):
        arguments_parser.add_argument('--temperature',
                                      type=float, default=-1.0,
                                      help="Generation 'temperature'. If not specified, the previously specified value (or 0.0) will be used.")
        arguments_parser.add_argument('--model',
                                      type=str, default="",
                                      help=f"Generation 'model' name. If not specified, the previously specified value（or {self.default_parameters['model']}) will be used.")

    def agent(self, line, cell, local_ns=None):
        arguments_parser = create_argument_parser(
            prog='%%agent', line=line,
            description='Give arbitrary instructions to the assistant. '
                        'Please write instructions for the assistant on the second and subsequent lines.'
        )
        self.__add_agent_params_to(arguments_parser)
        arguments = arguments_parser.get_arguments()
        if arguments is None:
            return

        # 会話履歴にユーザメッセージを追加
        current_timestamp = datetime.now().isoformat()
        self.messages.append(Message(role='user', content=f"{current_timestamp} : {cell}", timestamp=current_timestamp))

        # エージェント実行
        self._do_agent(temperature=arguments.temperature, model=arguments.model)

    def _do_agent(self, temperature, model):
        # 保存可能なパラメタを取得
        if not model:
            model = self.default_parameters['model']
        if temperature < 0:
            temperature = self.default_parameters['temperature']

        # 実行
        new_messages = query_to_agent(
            messages=self.messages,
            function_executor=self.get_tool_executor(),
            temperature=temperature,
            model=model,
            stream_handler_class=self.get_stream_handler_class()
        )

        # 会話履歴に追加
        self.messages.extend(new_messages)

        # 会話履歴保存
        conversation_history_util.save(self.messages, self.get_conversation_history_json_path())

        # デフォルトパラメータ保存
        self.default_parameters['temperature'] = temperature
        self.default_parameters['model'] = model
        save_default_parameters(self.default_parameters)

        # トークン使用量に留意
        total_token_count = conversation_history_util.get_token_count(self.messages)
        if total_token_count > 132000 - 4096 * 2:
            display(Markdown("** The remaining memory for the Assistant's conversation history is low. ** \n\n"
                             "The '%reset_conversation_history' command allows you to discard previous conversation history and restore remaining memory capacity. "))

    def resume(self, line):
        arguments_parser = create_argument_parser(
            prog='%%agent', line=line,
            description='Let assistant output to continue without additional user instructions. Use this command when the assistant outputs only the plan and then stops.'
        )
        self.__add_agent_params_to(arguments_parser)
        arguments = arguments_parser.get_arguments()
        if arguments is None:
            return

        self._do_agent(temperature=arguments.temperature, model=arguments.model)

    def redo(self, line):
        arguments_parser = create_argument_parser(
            prog='%%agent', line=line,
            description='Delete the last output and regenerate with the same input as last time and new parameter if specified it. However, the results of tools run by the assistant remain.'
        )
        self.__add_agent_params_to(arguments_parser)
        arguments = arguments_parser.get_arguments()
        if arguments is None:
            return

        self._remove_last_outputs(remove_last_user_message=False)
        self._do_agent(temperature=arguments.temperature, model=arguments.model)

    def undo(self, line):
        arguments_parser = create_argument_parser(
            prog='%%agent', line=line,
            description='Delete the last input and output. However, the results of tools run by the assistant remain.'
        )
        arguments = arguments_parser.get_arguments()
        if arguments is None:
            return

        self._remove_last_outputs(remove_last_user_message=True)

    def _remove_last_outputs(self, remove_last_user_message: bool = False):
        messages_to_remove = list()
        # 最後のrole=userのメッセージの直後までを削除対象とする
        for i in range(len(self.messages) - 1, -1, -1):
            message = self.messages[i]
            if message.role == 'user':
                if remove_last_user_message:
                    messages_to_remove.append(message)
                break
            else:
                messages_to_remove.append(message)
        # 削除する
        for message in messages_to_remove:
            self.messages.remove(message)
        # 会話履歴保存
        conversation_history_util.save(self.messages, self.get_conversation_history_json_path())
        # 処理結果を表示
        print(f'Removed the last {len(messages_to_remove)} output messages from the conversation history.')

    def get_stream_handler_class(self):
        return StreamHandler


def function_schema(description: str):
    def decorator(func: Callable):
        sig = inspect.signature(func)
        parameters = {'type': "object", 'properties': {}, 'required': []}
        for param_name, param in sig.parameters.items():
            param_type = param.annotation
            param_schema = type_to_json_schema(param_type, param_name)
            parameters['properties'][param_name] = param_schema
            if param.default == param.empty:
                parameters['required'].append(param_name)

        func.schema = {
            'name': func.__name__,
            'description': description,
            'parameters': parameters,
        }

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def type_to_json_schema(py_type, name: str):
    origin_type = typing.get_origin(py_type)
    if is_dataclass(py_type):
        properties = {}
        required = []
        for field in fields(py_type):
            properties[field.name] = type_to_json_schema(field.type, field.name)
            if 'description' in field.metadata:
                properties[field.name]['description'] = field.metadata['description']
            if field.default == field.default_factory:
                required.append(field.name)
        return {
            "type": "object",
            "properties": properties,
            "required": required
        }
    elif origin_type is list:
        # リストの要素の型を取得
        generic_args = typing.get_args(py_type)
        if generic_args:
            # リストの要素の型に基づいてスキーマを生成
            item_type = type_to_json_schema(generic_args[0], f'{name}[0]')
            return {"type": "array", "items": item_type}

    elif py_type == str:
        return {"type": "string"}
    elif py_type == int:
        return {"type": "integer"}
    elif py_type == float:
        return {"type": "number"}
    elif py_type == bool:
        return {"type": "boolean"}
    elif py_type == list:
        return {"type": "array"}
    else:
        raise NotImplementedError(
            f"No type annotation specified for argument or property {name}. Function arguments decorated with function_schema must (recursively) have type annotations.")
    # その他の型に対する変換を必要に応じて追加


def type_and_dict_to_value(py_type, value):
    try:
        origin_type = typing.get_origin(py_type)
        if is_dataclass(py_type):
            # データクラスの場合
            # データクラスのフィールドの型に基づいて値を生成
            # return py_type(**{
            #     field.name: type_and_dict_to_value(field.type, value.get(field.name) if value is not None else None)
            #     for field in fields(py_type)
            # })
            constructor_args = dict()
            for field in fields(py_type):

                # field_value = value.get(field.name) if value is not None else None
                if value is not None:
                    field_value = value.get(field.name)
                else:
                    if field.default_factory is not None:
                        field_value = field.default_factory()
                    else:
                        field_value = field.default
                constructor_args[field.name] = type_and_dict_to_value(field.type, field_value)
            return py_type(**constructor_args)

        elif origin_type is list:
            # リストの要素の型を取得
            generic_args = typing.get_args(py_type)
            if generic_args:
                # リストの要素の型に基づいて値を生成
                return [type_and_dict_to_value(generic_args[0], item) for item in value]
        elif py_type == str:
            return str(value)
        elif py_type == int:
            return int(value)
        elif py_type == float:
            return float(value)
        elif py_type == bool:
            return bool(value)
        elif py_type == list:
            return list(value)
        else:
            raise NotImplementedError(
                f"No valid type annotation specified for argument or property ({py_type}) (function arguments decorated with function_schema must (recursively) have type annotations)")
        # その他の型に対する変換を必要に応じて追加
    except Exception as e:
        logger.exception(f"Failed to convert value to {py_type} : {value}", e)

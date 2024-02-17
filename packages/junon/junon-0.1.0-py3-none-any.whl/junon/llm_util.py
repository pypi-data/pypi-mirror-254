import json
import logging
import os
from dataclasses import dataclass, is_dataclass
from typing import List, Dict, Optional, Union
from IPython.core.display import Markdown, TextDisplayObject
from IPython.lib.display import Code
import openai
from openai import OpenAI, AzureOpenAI
from openai._types import NOT_GIVEN
from openai.types import CompletionUsage
from openai.types.chat import ChatCompletionChunk
from openai.types.chat.chat_completion_chunk import Choice, ChoiceDeltaFunctionCall
from IPython.core.display_functions import clear_output, display, update_display
from junon.util.conversation_history_util import Message
from openai.types.chat.chat_completion_message import FunctionCall
from junon.util.structured_data import asdict2
import junon.util.ai_config_util

if os.environ.get('AZURE_OPENAI_API_KEY'):
    # デフォルトモデル変更
    if os.environ.get('AZURE_OPENAI_DEFAULT_MODEL'):
        junon.util.ai_config_util.DEFAULT_MODEL = os.environ['AZURE_OPENAI_DEFAULT_MODEL']
        from junon.util.ai_config_util import DEFAULT_MODEL
    # 初期化
    client = AzureOpenAI(
        api_key=os.environ['AZURE_OPENAI_API_KEY'],
        api_version="2023-12-01-preview",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),

    )
    print('Azure-OpenAI client initiated.')
else:
    from junon.util.ai_config_util import DEFAULT_MODEL

    client = OpenAI()
    print('OpenAI client initiated')

logger = logging.getLogger(__name__)


class CompletionResult:
    def __init__(self, content: str = "", usage: Optional[CompletionUsage] = None,
                 function_call: Optional[FunctionCall] = None):
        self.role = None
        self.content = content
        self.usage: Optional[CompletionUsage] = usage
        self.function_call: Optional[FunctionCall] = function_call


class StreamHandler:
    def __init__(self):
        self.result: CompletionResult = CompletionResult()
        self.current_calling_function_name: Optional[str] = None
        self.output_handles = list()
        self.displayed_objects: List[TextDisplayObject] = list()

    def on_chunk(self, chunk: ChatCompletionChunk):
        # チャンクをパース
        chunk_choice: Choice = chunk.choices[0]

        # role処理
        chunk_role = chunk_choice.delta.role
        if chunk_role:
            # 処理
            self.result.role = chunk_role

        # content断片を処理
        chunk_content = chunk_choice.delta.content
        if chunk_content:
            self.result.content += chunk_content

        # function_callを処理
        chunk_function_call = chunk_choice.delta.function_call
        if chunk_function_call:
            if self.result.function_call is None:
                self.result.function_call = FunctionCall(name="", arguments="")
            if chunk_function_call.name:
                self.result.function_call.name = chunk_function_call.name
                self.current_calling_function_name = chunk_function_call.name
            if chunk_function_call.arguments:
                self.result.function_call.arguments += chunk_function_call.arguments

        # usageを処理
        if self.result.usage is None:
            self.result.usage = CompletionUsage(
                completion_tokens=0,
                prompt_tokens=0,
                total_tokens=0,
            )
        self.result.usage.completion_tokens += 1

        # 表示する要素を取得
        display_objs = self.get_display_objects(message=None)
        # 表示ハンドラ, キャッシュが不足していたらその分だけ追加
        len_handles = len(self.output_handles)
        len_new_disps = len(display_objs)
        len_old_disps = len(self.displayed_objects)
        while len_handles < len_new_disps:
            self.output_handles.append(display(Markdown(''), display_id=True))
            len_handles += 1
        while len_old_disps < len_new_disps:
            self.displayed_objects.append(Markdown(''))
            len_old_disps += 1
        # 表示（更新）
        for handle, new_obj, old_obj in zip(self.output_handles, display_objs, self.displayed_objects):
            if new_obj.data != old_obj.data:  # ちらつき軽減のため、変更があった場合のみ更新
                update_display(new_obj, display_id=handle.display_id)
        # キャッシュを更新
        self.displayed_objects = display_objs

    def get_display_objects(self, message: Optional[Union[Message, Dict]] = None) -> List[TextDisplayObject]:
        """
        表示用のオブジェクト（のリスト）を取得する
        :param message: Noneの場合は、self.resultを使う
        :return:
        """
        if message is None:
            message = Message.from_dict(dict(
                role=self.result.role,
                content=self.result.content,
                function_call=self.result.function_call,
            ))
        if isinstance(message, dict):
            message = Message.from_dict(message)

        # 結果リストを初期化
        result: List[TextDisplayObject] = list()

        # 区切り線
        result.append(self.get_display_message_divider_part(message))

        # ヘッダー
        result.append(self.get_display_message_header_part(message))

        # 本文
        if message.content:
            result.extend(self.get_display_message_content_parts(message))

        # 関数呼び出し
        if message.function_call:
            result.extend(self.get_display_message_function_call_parts(message))

        return result

    def on_finished(self, finish_reason: str, messages: List[Union[Message, Dict]]) -> bool:
        logger = logging.getLogger(__name__)
        # 終了または継続
        if finish_reason == 'length':
            logger.info('return True (continue generation)')
            return True
        else:
            logger.info('return False (finish generation)')
            return False

    def get_result(self) -> CompletionResult:
        return self.result

    def get_display_message_divider_part(self, message: Message) -> TextDisplayObject:
        return Markdown("\n\n----------------------------------------\n\n")

    def get_display_message_header_part(self, message: Message) -> TextDisplayObject:
        if message.role == 'assistant':
            # role_emoji = '&#x1F4CE;'  # クリップ
            role_emoji = '&#x1F481;'  # Helpdesk
        elif message.role == 'system':
            role_emoji = '&#x1F935;'  # Man in tuxedo
        elif message.role == 'user':
            role_emoji = '&#x1F464;'  # Bust
        elif message.role == 'function':
            role_emoji = '&#x1F916;'  # Robot
        else:
            role_emoji = ''

        name = f"{role_emoji} **{message.role}** " + (f' [ `{message.name}` ]' if message.name else '')
        md = f"{name} : \n"
        return Markdown(md)

    def get_display_message_content_parts(self, message: Message) -> List[TextDisplayObject]:
        result: List[TextDisplayObject] = list()
        if message.role == 'function':
            result.append(Markdown('**function response :**'))
            result.append(Code(data=message.content, language='json'))
        else:
            result.append(Markdown(message.content))
        return result

    # get_display_message_function_call_parts
    def get_display_message_function_call_parts(self, message: Message) -> List[TextDisplayObject]:
        result: List[TextDisplayObject] = list()

        function_call = message.function_call
        if function_call:
            if function_call.name:
                result.append(Markdown(f'**request function :** to `{function_call.name}`'))
            if function_call.arguments:
                result.append(Code(data=function_call.arguments, language='json'))
        return result

    def display_message(self, message: Union[Message, Dict]):
        display_objs = self.get_display_objects(message)
        for display_obj in display_objs:
            display(display_obj)


def query_to_agent(
        model: str = DEFAULT_MODEL,
        temperature: float = 0.0,
        messages: List[Message] = None,
        function_executor=None,  # 循環参照になるので、型アノテーションのためだけにFunctionExecutorをimportしない
        stream_handler_class=StreamHandler,
) -> List[Message]:
    new_messages: List[Message] = list()

    continue_loop = True

    while continue_loop:
        # デフォルトではループ無し
        continue_loop = False
        # 生成
        sh = stream_handler_class()
        retry_count = 0
        completion_result = None
        functions = function_executor.get_functions_definition() if function_executor else NOT_GIVEN
        logger.debug('functions')
        logger.debug(json.dumps(functions, indent=4, ensure_ascii=False))
        while retry_count < 3:
            try:
                completion_result = do_completion(
                    stream_handler=sh,
                    model=model,
                    functions=functions,
                    temperature=temperature,
                    messages=Message.list_to_api_argument(messages + new_messages),
                )
                break
            except Exception as e:
                retry_count += 1
                logger.warning(f"Error in completion: {type(e)} : {e}")
                if retry_count >= 3:
                    raise e

        # 生成結果を追加
        new_messages.append(Message.from_dict(dict(
            role=completion_result.role,
            content=completion_result.content,
            function_call=completion_result.function_call,
        )))

        # 必要に応じて関数実行
        if completion_result.function_call:
            function_execution_result = function_executor.execute(
                function_name=completion_result.function_call.name,
                arguments_json=completion_result.function_call.arguments,
            )
            # dataclassなら、dictに変換(違ったらそのまま)
            function_execution_result = asdict2(function_execution_result)

            # dataclassをjson.dumpsするためのエンコーダ関数を準備
            def json_encoder(x):
                if is_dataclass(x):
                    if hasattr(x, '__hash__'):
                        return x.__hash__()
                    else:
                        return asdict2(x)
                else:
                    return x

            # 結果メッセージを追加
            function_execution_result_message = Message.from_dict(dict(
                role='function',
                name=completion_result.function_call.name,
                content=json.dumps(function_execution_result, default=json_encoder, indent=4, ensure_ascii=False),
            ))
            new_messages.append(function_execution_result_message)
            # 結果メッセージを表示
            sh = stream_handler_class()
            sh.display_message(function_execution_result_message)
            # 継続（結果を受けて次の生成をする）
            continue_loop = True

    return new_messages


def do_completion(
        stream_handler: Optional[StreamHandler],
        model: str = DEFAULT_MODEL,
        functions: List[Dict] = NOT_GIVEN,
        temperature: float = 0.0,
        messages: List[Dict] = None,
        response_format: Optional[Dict] = NOT_GIVEN,
) -> CompletionResult:
    logger = logging.getLogger(__name__)
    logger.info('do_completion')

    new_messages: List[Dict] = []
    continue_required = True
    while continue_required:
        logger.info(f"completion start ...")
        # logger.debug("messages:")
        # for m in messages_work:
        #     log_name = m.get('role') + (('/' + m.get('name')) if m.get('name') else '')
        #     logger.debug(f"* {log_name} : {m.get('content') or m.get('function_call')}")
        # logger.debug(f"functions:")
        # logger.debug(json.dumps(functions, indent=4, ensure_ascii=False))

        # # 補完呼び出しごとにプログレスバー初期化
        # progress_bar = tqdm(total=4096)

        # APIにリクエスト
        continue_required = False
        response = client.chat.completions.create(
            model=model,
            functions=functions,
            temperature=temperature,
            messages=messages + new_messages,
            response_format=response_format,
            max_tokens=4096,
            stream=True
        )

        # 結果処理
        for chunk in response:
            # # プログレス表示
            # progress_bar.update(1)
            # finish_reason取得
            if not chunk.choices:
                logger.debug(f'chunk.choices is empty : {chunk}')
                # azureの場合、フィルタ結果だけのchunkが返ってくることがある
                continue

            finish_reason = chunk.choices[0].finish_reason
            # チャンクを処理
            stream_handler.on_chunk(chunk)

            # トークン不足で終了した場合は継続する
            if finish_reason:
                new_messages.append({"role": 'assistant', "content": stream_handler.get_result().content})
                continue_required = stream_handler.on_finished(finish_reason=finish_reason, messages=new_messages)
                break
        # progress_bar.close()

    return stream_handler.get_result()

import io
import json
import logging
import os
import platform
import subprocess
import textwrap
from dataclasses import dataclass, field
from typing import List, Dict, Union, Optional

from IPython import get_ipython
from IPython.core.interactiveshell import InteractiveShell, ExecutionResult
from contextlib import redirect_stdout, redirect_stderr

from IPython.core.display import Markdown, TextDisplayObject
from IPython.core.display_functions import display
from IPython.core.magic import magics_class, Magics, cell_magic, line_magic
from IPython.lib.display import Code
from openai.types.chat.chat_completion_chunk import ChoiceDeltaFunctionCall
from overrides import override

from junon.assistants import FunctionExecutor, AssistantMagicBase, function_schema, type_and_dict_to_value
from junon.llm_util import StreamHandler
from junon.util.conversation_history_util import Message
from junon.util.gpt_stream_parser import close_partial_json
from junon.util.structured_data import StructureData, StructureDataID
logger = logging.getLogger(__name__)

METADATA_DIR = os.path.join('.da')
CONVERSATION_HISTORY_JSON_PATH = os.path.join(METADATA_DIR, "conversation_history.json")
PROJECT_PREFERENCES_FILE = os.path.join(METADATA_DIR, f'project_preferences.json')

if not os.path.exists(METADATA_DIR):
    os.makedirs(METADATA_DIR)


@magics_class
class DataAnalyst(AssistantMagicBase, Magics):

    def __init__(self, shell):
        super().__init__(shell=shell, executor=_executor)

    def get_tool_executor(self) -> FunctionExecutor:
        return self.executor

    def get_conversation_history_json_path(self) -> str:
        return CONVERSATION_HISTORY_JSON_PATH

    def is_current_session_continued(self) -> bool:
        return os.path.exists(PROJECT_PREFERENCES_FILE)

    def system_message_on_init(self) -> str:
        os_name = platform.platform()
        return textwrap.dedent(
            f"""
            あなたはデータ分析アシスタントです。あなたの主な役割は、クライアントであるユーザーのデータ分析プロジェクトを支援することです。
            
            あなたとユーザーは、データの洞察と解釈を通じて特定の分析目標を達成することを目指すチームの一部です。
            
            ## あなたの目的
            
            ユーザーと協力して、データに基づいた洞察と意味ある結果を生み出すこと。
            
            ユーザーからのリクエストに応えるだけでなく、次のような場合にも**積極的に**行動してください：
            - データセットの構造、関連性、および可能な分析方法について提案する。
            - 誤ったデータ解釈や分析方法の修正を提案する。
            - ユーザーと協力して、データ分析のコンセプト、アプローチ、および結果を議論する。
            
            ただし、データ分析の最終的な解釈や使用方法に関しては、ユーザーの決定に従ってください。
            
            ## データ分析環境
            
            - あなたとユーザーは単一のデータ分析環境(Python/{os_name})を共有します。
            - この分析環境は各プロジェクトごとに独立しており、一つのプロジェクトのみをサポートします。
            - 分析環境内では、次のものをツールを通じて保存、参照、実行することができます：
                - プロジェクト設定情報の保存/参照：
                - Pythonコードの実行：run_code_cell
                - シェルコマンドの実行、ファイルシステムへのアクセス：run_shell_commandなど
                
            - あなたの記憶容量は限られているため、ツールを使用してこれらの成果物を常に保存してください。            """
        )

    def system_message_on_new_start(self) -> str:
        return textwrap.dedent(
            """
            ---
            それでは始めてください。
            まずは簡単な挨拶をしましょう。その後、このデータ分析プロジェクトの概要についてユーザーに尋ねてください。
            その際、一度に多くの質問をするのではなく、ユーザーの反応を見ながら徐々に質問を行ってください。
            ユーザーの反応に基づいて、データセット、分析の目的、または特に注目している点について掘り下げて質問すると良いでしょう。
            """
        )

    def system_message_on_continue(self) -> str:
        return textwrap.dedent(
            """
            ---
            たった今、あなたは進行中のデータ分析プロジェクトを引き継ぎました。
            以前のアシスタントとユーザー間の会話履歴を参照することはできませんが、
            ツールを通じてデータ分析環境に保存されている様々なデータにアクセスすることが可能です。
            まずは簡単な挨拶をし、自分の状況をユーザーに説明してください。
            その後、プロジェクトの進行方法についてユーザーと話し合ってください。
            """
        )

    def get_stream_handler_class(self):
        return StreamDisplayHandlerImpl

    @line_magic
    def usage(self, line):
        super().usage(line)

    @cell_magic
    def agent(self, line, cell, local_ns=None):
        super().agent(line, cell, local_ns)

    @line_magic
    def resume(self, line):
        super().resume(line)

    @line_magic
    def undo(self, line):
        super().undo(line)

    @line_magic
    def redo(self, line):
        super().redo(line)

    @line_magic
    def history(self, line):
        super().history(line)

    @line_magic
    def reset_conversation_history(self, line):
        super().reset_conversation_history(line)


@dataclass
class ProjectPreferences:
    project_title: str = ''
    user_communication_language: str = ''
    code_comment_language: str = ''
    overview: str = ''


@function_schema("Save project preferences to writing environment")
def save_writing_project_preferences(preferences: ProjectPreferences, overwrite: bool = False):
    filename = PROJECT_PREFERENCES_FILE

    if os.path.exists(filename) and not overwrite:
        raise FileExistsError(f"Preferences exists: {filename}")

    if os.path.exists(filename):
        # 既存のファイルがある場合は、一度読み込んでから上書きする
        with open(filename, 'r') as file:
            file_data = json.load(file)
            # dictとしてマージ
            data = {**file_data, **preferences.__dict__}
            # 変換
            preferences = ProjectPreferences(**data)

    with open(filename, 'w') as file:
        json.dump(preferences, file, indent=4, default=lambda x: x.__dict__)
    return dict(result='saved or overwritten successfully')


@function_schema("Load project preferences from writing environment")
def load_writing_project_preferences() -> ProjectPreferences:
    filename = PROJECT_PREFERENCES_FILE

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Preferences file not found")

    with open(filename, 'r') as file:
        data = json.load(file)
        return ProjectPreferences(**data)


# ------------------------------------
# シェルコマンド実行系
# ------------------------------------
@dataclass
class RunShellCommandRequest:
    command_line: str = ''


@dataclass
class RunShellCommandResult:
    stdout: str = ''
    stderr: str = ''
    return_code: int = 0


@function_schema("Run shell command in data analytics environment")
def run_shell_command(request: RunShellCommandRequest) -> RunShellCommandResult:
    # Run shell command with subprocess and return stdout and stderr
    try:
        # 実行するコマンド
        completed_process = subprocess.run(
            request.command_line,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True
        )

        # 標準出力と標準エラー出力を取得
        stdout = completed_process.stdout
        stderr = completed_process.stderr
        return_code = completed_process.returncode

    except subprocess.CalledProcessError as e:
        # エラーが発生した場合は、その内容を含める
        stdout = e.stdout
        stderr = e.stderr
        return_code = e.returncode

    return RunShellCommandResult(stdout=stdout, stderr=stderr, return_code=return_code)


@dataclass
class TreeRequest:
    path: str = ''


@dataclass
class TreeResult:
    tree: str = ''


@function_schema("Get directory tree as string")
def tree(request: TreeRequest) -> TreeResult:
    return TreeResult(tree=build_tree_string(request.path))


def build_tree_string(directory, prefix=''):
    if not os.path.isdir(directory):
        raise ValueError(f"'{directory}' is not a valid directory.")

    tree_str = ""
    files = []
    if os.path.isdir(directory):
        files = os.listdir(directory)

    for i, file in enumerate(files):
        path = os.path.join(directory, file)
        is_last = i == (len(files) - 1)
        if os.path.isdir(path):
            # ディレクトリの場合
            new_prefix = prefix + ('└── ' if is_last else '├── ')
            tree_str += prefix + ('└── ' if is_last else '├── ') + file + "\n"
            tree_str += build_tree_string(path, prefix + ('    ' if is_last else '│   '))
        else:
            # ファイルの場合
            tree_str += prefix + ('└── ' if is_last else '├── ') + file + "\n"

    return tree_str


@dataclass
class MakeDirectoriesRequest:
    path: str = ''


@function_schema("Make directories")
def make_directories(request: MakeDirectoriesRequest):
    os.makedirs(request.path, exist_ok=True)
    return dict(result='success')


# ------------------------------------
# Pythonコード実行系
# ------------------------------------

@dataclass
class RunPythonCodeRequest:
    cell_str: str = field(
        metadata={
            "description": "**REQUIRED** Whole code in the cell to run. Python code and/or magic command."
        }
    )


@dataclass
class RunPythonCodeResult:
    status: str = ''
    return_code: str = ''
    stdout: str = ''
    stderr: str = ''
    error_in_exec: str = ''


@function_schema("Run python code or magic command in data analytics environment (as a notebook cell)")
def run_code_cell(request: RunPythonCodeRequest) -> RunPythonCodeResult:
    # Run Python code with exec and return stdout and stderr
    stdout = io.StringIO()
    stderr = io.StringIO()
    try:
        # コードを実行し、出力とエラーをキャプチャ
        ip = get_ipython()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            result: ExecutionResult = ip.run_cell(
                raw_cell=request.cell_str,
                store_history=False,
                silent=True,
                shell_futures=False,
            )

        # キャプチャされた出力とエラーを取得
        captured_output = stdout.getvalue()
        captured_error = stderr.getvalue()

        return RunPythonCodeResult(
            status='success' if result.success else 'error',
            stdout=captured_output,
            stderr=captured_error,
            error_in_exec=result.error_in_exec.__repr__() if result.error_in_exec else ''
        )

    except Exception as e:
        # エラーが発生した場合は、その内容を含める
        captured_output = stdout.getvalue()
        captured_error = stderr.getvalue()
        return RunPythonCodeResult(
            status='system_error',
            stdout=captured_output,
            stderr=captured_error,
            error_in_exec=e.__repr__()
        )


_executor = FunctionExecutor(
    functions=[
        # 執筆プロジェクトの設定情報
        save_writing_project_preferences,
        load_writing_project_preferences,
        # シェルコマンド系
        run_shell_command,
        tree,
        make_directories,
        # Pythonコード実行系
        run_code_cell,
    ]
)


# ------------------------------------
# StreamHandler
# for display customization
# ------------------------------------

class StreamDisplayHandlerImpl(StreamHandler):
    def __init__(self):
        super().__init__()

    @override
    def get_display_message_function_call_parts(self, message: Message) -> List[TextDisplayObject]:
        result: List[TextDisplayObject] = list()

        function_call = message.function_call
        if function_call:
            if function_call.name == 'run_code_cell':
                try:
                    # コード部分をコードブロックとして表示する
                    if function_call.name:
                        result.append(Markdown(f'**request function :** to `{function_call.name}`'))
                    if function_call.arguments:
                        arguments = json.loads(
                            # assistant応答はstreamなのでjsonが不完全かもしれない
                            close_partial_json(function_call.arguments)
                        )
                        request_str = arguments.get('request')
                        request_str = close_partial_json(request_str)
                        request: RunPythonCodeRequest = type_and_dict_to_value(RunPythonCodeRequest, request_str)
                        result.append(Markdown('**Running code cell :**'))
                        result.append(Code(data=request.cell_str, language='python'))
                except Exception as e:
                    # jsonの強制パースが失敗する場合はデフォルト
                    return super().get_display_message_function_call_parts(message)
            else:
                # それ以外はデフォルト動作
                return super().get_display_message_function_call_parts(message)

        return result

    @override
    def get_display_message_content_parts(self, message: Message) -> List[TextDisplayObject]:
        if message.name == 'run_code_cell':
            result: List[TextDisplayObject] = list()
            # コード実行結果をコードブロックとして表示する
            content_obj = json.loads(message.content)
            run_result: RunPythonCodeResult = type_and_dict_to_value(RunPythonCodeResult, content_obj)
            if run_result:
                if run_result.stdout:
                    result.append(Markdown('**stdout :**'))
                    result.append(Code(data=run_result.stdout))
                if run_result.stderr:
                    result.append(Markdown('**stderr :**'))
                    result.append(Code(data=run_result.stderr))
                if run_result.error_in_exec:
                    result.append(Markdown('**error_in_exec :**'))
                    result.append(Code(data=run_result.error_in_exec))
            return result
        else:
            # それ以外はデフォルト動作
            return super().get_display_message_content_parts(message)


def load_ipython_extension(ipython):
    """
    コードセルで以下を実行すると、DataAnalystをnotebookで使用できるようになります。
    ```
    %load_ext junon.assistants.writing_assistant
    ```
    :param ipython:
    :return:
    """
    ipython.register_magics(DataAnalyst)

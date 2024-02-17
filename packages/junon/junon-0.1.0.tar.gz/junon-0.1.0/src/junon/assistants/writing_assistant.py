import json
import logging
import os
import textwrap
from dataclasses import dataclass, field
from typing import List, Dict

from IPython.core.display import TextDisplayObject, Markdown
from IPython.core.magic import magics_class, Magics, cell_magic, line_magic
from IPython.lib.display import Code
from openai.types.chat.chat_completion_chunk import ChoiceDeltaFunctionCall
from overrides import override

from junon.assistants import FunctionExecutor, AssistantMagicBase, function_schema, type_and_dict_to_value
from junon.llm_util import StreamHandler
from junon.util.conversation_history_util import Message
from junon.util.gpt_stream_parser import close_partial_json
from junon.util.structured_data import StructureData, StructureDataID

METADATA_DIR = os.path.join('.junon')
CONVERSATION_HISTORY_JSON_PATH = os.path.join(METADATA_DIR, "conversation_history.json")
PROJECT_PREFERENCES_FILE = os.path.join(METADATA_DIR, f'project_preferences.json')
CONCEPT_DIR = os.path.join(METADATA_DIR, 'concept_proposals')
MANUSCRIPTS_DIR = os.path.join(METADATA_DIR, 'manuscripts')

if not os.path.exists(METADATA_DIR):
    os.makedirs(METADATA_DIR)
if not os.path.exists(CONCEPT_DIR):
    os.makedirs(CONCEPT_DIR)
if not os.path.exists(MANUSCRIPTS_DIR):
    os.makedirs(MANUSCRIPTS_DIR)


@magics_class
class WritingAssistant(AssistantMagicBase, Magics):

    def __init__(self, shell):
        super().__init__(shell=shell, executor=_executor)

    def get_tool_executor(self) -> FunctionExecutor:
        return self.executor

    def get_conversation_history_json_path(self) -> str:
        return CONVERSATION_HISTORY_JSON_PATH

    def is_current_session_continued(self) -> bool:
        return os.path.exists(PROJECT_PREFERENCES_FILE)

    def system_message_on_init(self) -> str:
        return textwrap.dedent(
            """
            You are a writing assistant. Your primary job is to support the user, who is your client, in their writing endeavors.
            
            You and the user are part of a team with a common goal: the completion of a single writing project.
            
            ## Your Objectives
            
            Aim to create better written works in collaboration with the client (user).
            
            Not only when requested by the user, but also when you feel it's necessary, **proactively** engage in the following:
            - Propose ideas regarding the concept, structure, and draft of the writing to the user.
            - Ask questions and organize information. If there are any inconsistencies with previously discussed and agreed-upon content, work together with the user to make corrections.
            - Discuss the concept, structure, and draft of the writing with the user.
            
            However, please follow the user's decisions regarding the final determination of the writing.
            
            ## Writing Environment
            
            - You and the user share a single writing environment.
            - The writing environment is independent for each writing project, and this environment supports only one writing project.
            - Within the writing environment, you can save and refer to the following through tools:
                - Project settings information
                - Concept ideas for the writing
                - Chapter information
                - Section information
                - Topic information
                - Paragraph information
            - Note: The written material is managed in a hierarchical structure of Chapters > Sections > Topics > Paragraphs.
            - As your memory capacity is limited, always make sure to save these (intermediate) outputs using the tools provided.
            """
        )

    def system_message_on_new_start(self) -> str:
        return textwrap.dedent(
            """
            ---
            Please begin. 
            Start by offering a simple greeting and then proceed to ask the user about the overview of this writing project. 
            When doing so, avoid bombarding them with too many questions at once. 
            Instead, observe the user's responses and gradually ask your questions.
            """
        )

    def system_message_on_continue(self) -> str:
        return textwrap.dedent(
            """
            ---
            Now, you have taken over an ongoing writing project. 
            While you cannot refer to the conversation history between the previous assistant and the user, 
            you can access various data stored in the writing environment through tools. 
            Begin with a simple greeting and explain your situation to the user. 
            Then, discuss with the user how to proceed with the project.
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
    writing_contents_language: str = ''
    overview: str = ''
    concept_proposal_adopted: int = field(default=-1, metadata={"description": "'** REQUIRED: ** Concept proposal number adopted by the user. -1 means not adopted yet.'"})


@function_schema("Save project preferences to writing environment")
def save_writing_project_preferences(preferences: ProjectPreferences, overwrite: bool = False):
    filename = PROJECT_PREFERENCES_FILE

    if os.path.exists(filename) and not overwrite:
        raise FileExistsError(f"Preferences exists: {filename}")

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
# データ構造
# ------------------------------------


@dataclass
class ParagraphID(StructureDataID):
    chapter_number: int = field(metadata={"description": "**REQUIRED:** Chapter number."})
    section_number: int = field(metadata={"description": "**REQUIRED:** Section number."})
    topic_number: int = field(metadata={"description": "**REQUIRED:** Topic number."})
    paragraph_number: int = field(metadata={"description": "**REQUIRED:** Paragraph number."})

    def dir_path(self):
        return os.path.join(
            MANUSCRIPTS_DIR,
            f'chapter_{self.chapter_number:02d}',
            f'section_{self.section_number:02d}',
            f'topic_{self.topic_number:02d}',
            f'paragraph_{self.paragraph_number:02d}'
        )

    def children_id_class(self):
        return None

    @classmethod
    def lowest_id_number_name(cls):
        return 'paragraph_number'

    def __hash__(self):
        return hash((self.chapter_number, self.section_number, self.topic_number, self.paragraph_number))


@dataclass
class Paragraph(StructureData[ParagraphID]):
    text: str = field(metadata={"description": "**REQUIRED:** Markdown text. "}, default='')
    tags: List[str] = field(metadata={"description": "Used when extract 'Index' from manuscript"}, default_factory=list)


@dataclass
class TopicID(StructureDataID):
    chapter_number: int = field(metadata={"description": "**REQUIRED:** Chapter number."})
    section_number: int = field(metadata={"description": "**REQUIRED:** Section number."})
    topic_number: int = field(metadata={"description": "**REQUIRED:** Topic number."})

    def dir_path(self):
        return os.path.join(
            MANUSCRIPTS_DIR,
            f'chapter_{self.chapter_number:02d}',
            f'section_{self.section_number:02d}',
            f'topic_{self.topic_number:02d}'
        )

    def children_id_class(self):
        return ParagraphID

    @classmethod
    def lowest_id_number_name(cls):
        return 'topic_number'

    def __hash__(self):
        return hash((self.chapter_number, self.section_number, self.topic_number))


@dataclass
class TopicMetadata(StructureData[TopicID]):
    title: str = field(metadata={"description": "**REQUIRED:** Topic title."}, default='')
    overview: str = field(metadata={"description": "Topic overview."}, default='')


@dataclass
class SectionID(StructureDataID):
    chapter_number: int = field(metadata={"description": "**REQUIRED:** Chapter number."})
    section_number: int = field(metadata={"description": "**REQUIRED:** Section number."})

    def dir_path(self):
        return os.path.join(
            MANUSCRIPTS_DIR,
            f'chapter_{self.chapter_number:02d}',
            f'section_{self.section_number:02d}'
        )

    def children_id_class(self):
        return TopicID

    @classmethod
    def lowest_id_number_name(cls):
        return 'section_number'

    def __hash__(self):
        return hash((self.chapter_number, self.section_number))


@dataclass
class SectionMetadata(StructureData[SectionID]):
    title: str = field(metadata={"description": "**REQUIRED:** Section title."}, default='')
    overview: str = field(metadata={"description": "Section overview."}, default='')


@dataclass
class ChapterID(StructureDataID):
    chapter_number: int = field(metadata={"description": "**REQUIRED:** Chapter number."})

    def dir_path(self):
        return os.path.join(
            MANUSCRIPTS_DIR,
            f'chapter_{self.chapter_number:02d}'
        )

    def children_id_class(self):
        return SectionID

    @classmethod
    def lowest_id_number_name(cls):
        return 'chapter_number'

    def __hash__(self):
        return hash((self.chapter_number,))


@dataclass
class ChapterMetadata(StructureData[ChapterID]):
    title: str = field(metadata={"description": "**REQUIRED:** Chapter title."}, default='')
    overview: str = field(metadata={"description": "Chapter overview."}, default='')


@dataclass
class ConceptID(StructureDataID):
    concept_proposal_number: int = field(metadata={"description": "**REQUIRED:** Concept proposal number."})

    def dir_path(self):
        return os.path.join(
            CONCEPT_DIR,
            f'concept_{self.concept_proposal_number:02d}'
        )

    def children_id_class(self):
        return None

    def __hash__(self):
        return hash((self.concept_proposal_number,))


@dataclass
class ConceptProposal(StructureData[ConceptID]):
    title: str = field(metadata={"description": "**REQUIRED:** Concept proposal title."}, default='')
    tagline: str = field(metadata={"description": "**REQUIRED:** Concept proposal tagline."}, default='')
    targetAudience: str = field(metadata={"description": "**REQUIRED:** Target audience."}, default='')
    overview: str = field(metadata={"description": "**REQUIRED:** Concept proposal overview."}, default='')
    writingStyle: str = field(metadata={"description": "**REQUIRED:** Writing style."}, default='')
    examplesOfWritingStyle: List[str] = field(metadata={"description": "**REQUIRED:** Examples of writing style."},
                                              default_factory=list)
    notesForManuscriptPreparation: List[str] = field(
        metadata={"description": "**REQUIRED:** Notes for manuscript preparation."}, default_factory=list)


# ------------------------------------
# コンセプト案の操作用関数
# ------------------------------------


@function_schema("Save concept proposal to writing environment")
def save_concept_proposal(concept_id: ConceptID, concept: ConceptProposal, overwrite: bool = False):
    return concept.save_as(concept_id, overwrite)


@function_schema("Load concept proposal from writing environment")
def load_concept_proposal(concept_id: ConceptID) -> ConceptProposal:
    return ConceptProposal.load_from(concept_id)


@function_schema("Get list of concept proposals from writing environment")
def list_concept_proposal() -> Dict[ConceptID, ConceptProposal]:
    return ConceptProposal.list_data(
        parent_id_or_root_dir=CONCEPT_DIR,
        item_id_class=ConceptID
    )


@function_schema("Delete concept proposal from writing environment")
def delete_concept_proposal(concept_id: ConceptID):
    return ConceptProposal.delete(concept_id)


@function_schema("Move concept proposal to another directory in writing environment")
def move_concept_proposal(concept_id: ConceptID, new_concept_id: ConceptID, overwrite: bool = False):
    return ConceptProposal.move(concept_id, new_concept_id, overwrite)


# ------------------------------------
# Functions for Chapter
# ------------------------------------

@function_schema("Save chapter metadata to writing environment")
def save_chapter_metadata(chapter_id: ChapterID, chapter: ChapterMetadata, overwrite: bool = False):
    return chapter.save_as(chapter_id, overwrite)


@function_schema("Load chapter metadata from writing environment")
def load_chapter_metadata(chapter_id: ChapterID) -> ChapterMetadata:
    return ChapterMetadata.load_from(chapter_id)


@function_schema("Get list of chapter metadata from writing environment")
def list_chapter_metadata() -> Dict[ChapterID, ChapterMetadata]:
    return ChapterMetadata.list_data(
        parent_id_or_root_dir=MANUSCRIPTS_DIR,
        item_id_class=ChapterID
    )


@function_schema("Delete chapter metadata from writing environment")
def delete_chapter(chapter_id: ChapterID, include_subitems: bool = False):
    return ChapterMetadata.delete(
        data_id=chapter_id,
        include_subitems=include_subitems
    )


@function_schema("Move chapter metadata to another directory in writing environment")
def move_chapter(chapter_id: ChapterID, new_chapter_id: ChapterID, overwrite: bool = False):
    return ChapterMetadata.move(chapter_id, new_chapter_id, overwrite)


# ------------------------------------
# Functions for Section
# ------------------------------------

@function_schema("Save section metadata to writing environment")
def save_section_metadata(section_id: SectionID, section: SectionMetadata, overwrite: bool = False):
    return section.save_as(section_id, overwrite)


@function_schema("Load section metadata from writing environment")
def load_section_metadata(section_id: SectionID) -> SectionMetadata:
    return SectionMetadata.load_from(section_id)


@function_schema("Get list of section metadata from writing environment")
def list_section_metadata(chapter_id: ChapterID) -> Dict[SectionID, SectionMetadata]:
    return SectionMetadata.list_data(
        parent_id_or_root_dir=chapter_id,
        item_id_class=SectionID
    )


@function_schema("Delete section metadata from writing environment")
def delete_section(section_id: SectionID, include_subitems: bool = False):
    return SectionMetadata.delete(
        data_id=section_id,
        include_subitems=include_subitems
    )


@function_schema("Move section metadata to another directory in writing environment")
def move_section(section_id: SectionID, new_section_id: SectionID, overwrite: bool = False):
    return SectionMetadata.move(section_id, new_section_id, overwrite)


# ------------------------------------
# Functions for Topic
# ------------------------------------

@function_schema("Save topic metadata to writing environment")
def save_topic_metadata(topic_id: TopicID, topic: TopicMetadata, overwrite: bool = False):
    return topic.save_as(topic_id, overwrite)


@function_schema("Load topic metadata from writing environment")
def load_topic_metadata(topic_id: TopicID) -> TopicMetadata:
    return TopicMetadata.load_from(topic_id)


@function_schema("Get list of topic metadata from writing environment")
def list_topic_metadata(section_id: SectionID) -> Dict[TopicID, TopicMetadata]:
    return TopicMetadata.list_data(
        parent_id_or_root_dir=section_id,
        item_id_class=TopicID
    )


@function_schema("Delete topic metadata from writing environment")
def delete_topic(topic_id: TopicID, include_subitems: bool = False):
    return TopicMetadata.delete(
        data_id=topic_id,
        include_subitems=include_subitems
    )


@function_schema("Move topic metadata to another directory in writing environment")
def move_topic(topic_id: TopicID, new_topic_id: TopicID, overwrite: bool = False):
    return TopicMetadata.move(topic_id, new_topic_id, overwrite)


# ------------------------------------
# Functions for Paragraph
# ------------------------------------


@function_schema("Save paragraph to writing environment")
def save_paragraph(paragraph_id: ParagraphID, paragraph: Paragraph, overwrite: bool = False):
    return paragraph.save_as(paragraph_id, overwrite)


@function_schema("Load paragraph from writing environment")
def load_paragraph(paragraph_id: ParagraphID) -> Paragraph:
    return Paragraph.load_from(paragraph_id)


@function_schema("Get list of paragraph from writing environment")
def list_paragraph(topic_id: TopicID) -> Dict[ParagraphID, Paragraph]:
    return Paragraph.list_data(
        parent_id_or_root_dir=topic_id,
        item_id_class=ParagraphID
    )


@function_schema("Delete paragraph from writing environment")
def delete_paragraph(paragraph_id: ParagraphID):
    return Paragraph.delete(paragraph_id)


@function_schema("Move paragraph to another directory in writing environment")
def move_paragraph(paragraph_id: ParagraphID, new_paragraph_id: ParagraphID, overwrite: bool = False):
    return Paragraph.move(paragraph_id, new_paragraph_id, overwrite)


_executor = FunctionExecutor(
    functions=[
        # 執筆プロジェクトの設定情報
        save_writing_project_preferences,
        load_writing_project_preferences,
        # コンセプト案
        save_concept_proposal,
        load_concept_proposal,
        list_concept_proposal,
        delete_concept_proposal,
        move_concept_proposal,
        # チャプタ
        save_chapter_metadata,
        load_chapter_metadata,
        list_chapter_metadata,
        delete_chapter,
        move_chapter,
        # セクション
        save_section_metadata,
        load_section_metadata,
        list_section_metadata,
        delete_section,
        move_section,
        # トピック
        save_topic_metadata,
        load_topic_metadata,
        list_topic_metadata,
        delete_topic,
        move_topic,
        # パラグラフ
        save_paragraph,
        load_paragraph,
        list_paragraph,
        delete_paragraph,
        move_paragraph,
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
        function_call = message.function_call

        if function_call.name == 'save_paragraph':
            try:
                result: List[TextDisplayObject] = list()
                # 原稿保存時は、arguments[]がすでにマークダウンになっているので、そのまま表示。
                arguments = json.loads(
                    # assistant応答はstreamなのでjsonが不完全かもしれない
                    close_partial_json(function_call.arguments)
                )
                paragraph_id: ParagraphID = type_and_dict_to_value(ParagraphID, arguments.get('paragraph_id'))
                overwrite: bool = type_and_dict_to_value(bool, arguments['overwrite'])
                paragraph: Paragraph = type_and_dict_to_value(Paragraph, arguments['paragraph'])
                result.append(Markdown(f"** Saving paragraph ** : {paragraph_id} " + ('overwrite=True' if overwrite else '') + ' ...  \n\n'))
                result.append(Markdown(paragraph.text))
                return result
            except Exception as e:
                # jsonの強制パースが失敗する場合はデフォルト
                return super().get_display_message_function_call_parts(message)
        else:
            # それ以外はデフォルト動作
            return super().get_display_message_function_call_parts(message)


def load_ipython_extension(ipython):
    """
    コードセルで以下を実行すると、WritingAssistantをnotebookで使用できるようになります。
    ```
    %load_ext junon.assistants.writing_assistant
    ```
    :param ipython:
    :return:
    """
    ipython.register_magics(WritingAssistant)

import json
import os
import shutil
from abc import ABC, abstractmethod
from dataclasses import dataclass, is_dataclass, asdict
from typing import TypeVar, Generic, List, Union, Any, Dict


@dataclass
class StructureDataID(ABC):

    def file_path(self):
        return os.path.join(self.dir_path(), self.__class__.data_file_name())

    @classmethod
    def data_file_name(cls):
        return 'data.json'

    @abstractmethod
    def dir_path(self):
        pass

    @abstractmethod
    def children_id_class(self):
        """
        子階層のIDクラスを返します
        :return:
        """
        pass

    @classmethod
    def from_parent_and_dir_name(cls, parent, dir_name):
        if isinstance(parent, StructureDataID):
            id_values = parent.__dict__
        else:
            id_values = dict()

        # dir_nameから番号を取得
        lowest_id_number = int(dir_name.split('_')[-1])

        # コンストラクタのためのパラメタを完成
        id_values[cls.lowest_id_number_name()] = lowest_id_number

        # コンストラクタ呼び出し
        return cls(**id_values)

    @classmethod
    def lowest_id_number_name(cls):
        """
        このIDクラスの最下層のID番号の属性名を返します
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def __hash__(self):
        pass


# ジェネリック型パラメータTを定義
IDType = TypeVar('IDType', bound=StructureDataID)


@dataclass
class StructureData(Generic[IDType], ABC):

    def save_as(self, data_id: IDType, overwrite: bool = False):
        filename = data_id.file_path()
        if os.path.exists(filename) and not overwrite:
            raise FileExistsError(f"Duplicated id-number(s) : {id}")

        # 親ディレクトリがなければ再帰的に作る
        parent_dir = os.path.dirname(filename)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        with open(filename, 'w') as file:
            json.dump(self.__dict__, file, indent=4, ensure_ascii=False)
        return dict(result='saved successfully')

    @classmethod
    def load_from(cls, data_id: IDType):
        filename = data_id.file_path()

        if not os.path.exists(filename):
            raise FileNotFoundError(f"Not found id-number(s) : {data_id}")

        with open(filename, 'r') as file:
            data = json.load(file)
            return cls(**data)

    @classmethod
    def list_data(cls, parent_id_or_root_dir: Union[StructureDataID, str], item_id_class) -> Dict[
        IDType, 'StructureData']:
        """
        指定した親ID直下のデータをリストロードし、リストで返す
        :param parent_id_or_root_dir: Chapter一覧が欲しい時はNoneでよい。それ以外は親階層のIDが必要。
        :param item_id_class: 本階層のIDクラス
        :return:
        """
        if isinstance(parent_id_or_root_dir, StructureDataID):
            parent_dir = parent_id_or_root_dir.dir_path()
        else:
            parent_dir = parent_id_or_root_dir

        result = dict()
        sub_dir_list = [filename for filename in os.listdir(parent_dir) if
                        os.path.isdir(os.path.join(parent_dir, filename))]
        for sub_dir in sub_dir_list:
            sub_dir = os.path.join(parent_dir, sub_dir)
            data_file = os.path.join(sub_dir, item_id_class.data_file_name())
            if os.path.exists(data_file):
                item_id = item_id_class.from_parent_and_dir_name(parent_id_or_root_dir, sub_dir)
                with open(data_file, 'r') as file:
                    data = json.load(file)
                    result[item_id] = cls(**data)

        return result

    @classmethod
    def delete(cls, data_id: IDType, include_subitems: bool = False):
        file_path = data_id.file_path()
        dir_path = data_id.dir_path()
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Not found id-number(s) : {data_id}")

        if not include_subitems:
            # フラグがオフなら、子階層のデータがある場合は削除不可.
            # ディレクトリ内のサブディレクトリ一覧を確認する
            children_subdir = [filename for filename in os.listdir(dir_path) if
                               os.path.isdir(os.path.join(dir_path, filename))]
            if len(children_subdir) > 0:
                raise FileExistsError(f"Chapter {data_id.chapter_number} is not deletable. "
                                      f"Because subitems exists. "
                                      f"Please set include_subitems=True if you want to delete it.")

        # 親ディレクトリごと削除
        shutil.rmtree(dir_path)

        return dict(result=f"Succeeded to delete {data_id}")

    @classmethod
    def move(cls, src_id: IDType, dst_id: IDType, overwrite: bool = False):
        src_file = src_id.file_path()
        dst_file = dst_id.file_path()
        if src_file == dst_file:
            raise ValueError(f"Source and destination are same. src={src_id}, dst={dst_id}")
        if not os.path.exists(src_file):
            raise FileNotFoundError(f"Not found id-number(s) : {src_id}")
        if os.path.exists(dst_file) and not overwrite:
            raise FileExistsError(f"Duplicated id-number(s) : {dst_id}")

        src_dir = src_id.dir_path()
        dst_dir = dst_id.dir_path()

        # 先ディレクトリを削除(上書きチェック済)
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)

        # 移動
        shutil.move(src_dir, dst_dir)

        return dict(result=f"Succeeded to move {src_id} to {dst_id}")


def asdict2(input_data: Any) -> Any:
    if is_dataclass(input_data):
        # データクラスオブジェクトの場合、辞書に変換
        return asdict(input_data)
    elif isinstance(input_data, list):
        # リストの場合、各要素を処理
        return [asdict2(item) for item in input_data]
    elif isinstance(input_data, dict):
        # 辞書の場合、各値を処理
        return {key: asdict2(value) for key, value in input_data.items()}
    else:
        # データクラス、リスト、辞書以外の場合はそのまま返す
        return input_data

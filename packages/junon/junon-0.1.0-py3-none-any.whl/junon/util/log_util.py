import logging
import os
from logging.handlers import RotatingFileHandler


def init_for_wa(dir_name: str):
    # ログファイルのディレクトリとファイル名を設定
    log_directory = os.path.join(".junon", "logs", dir_name)
    log_file = os.path.join(log_directory, "log.txt")

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # ログフォーマットの設定
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    # ルートロガーの設定（ワーニング以上を標準エラー出力に）
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.handlers.clear()
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    root_logger.addHandler(console_handler)

    # 'hoge.fuga' パッケージ用ロガーの設定（全てのログをファイルに）
    hoge_fuga_logger = logging.getLogger('junon')
    hoge_fuga_logger.propagate = False
    hoge_fuga_logger.setLevel(logging.DEBUG)
    hoge_fuga_logger.handlers.clear()
    file_handler = RotatingFileHandler(log_file, maxBytes=1048576, backupCount=5)
    file_handler.setFormatter(log_format)
    hoge_fuga_logger.addHandler(file_handler)

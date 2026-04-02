import os

from sanguoagent.indexer import create_index, load_index, save_index
from sanguoagent.settings import Settings

settings = Settings()


def load_or_create_index():
    """构建或加载索引"""
    if (
        not os.path.exists(settings.VECTOR_STORE_DIR)
        or len(os.listdir(settings.VECTOR_STORE_DIR)) == 0
    ):
        print("正在构建索引...")
        index = create_index(settings.PROCESSED_DATA_DIR)
        save_index(index, settings.VECTOR_STORE_DIR)
        print("索引构建完成！")
    else:
        print("正在加载索引...")
        index = load_index(settings.VECTOR_STORE_DIR)
        print("索引加载完成！")
    return index

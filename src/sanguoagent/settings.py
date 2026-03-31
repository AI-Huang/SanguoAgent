import os

from dotenv import load_dotenv

from sanguoagent.utils import ensure_directory


class Settings:

    def __init__(self):
        if os.path.exists(".env.dev"):
            load_dotenv(".env.dev")

        # API 配置
        self.OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

        # 模型配置
        self.MODEL = os.getenv("MODEL", "text-embedding-3-small")

        # 索引配置
        self.CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
        self.CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

        # 数据目录配置
        self.DATA_DIR = os.path.expandvars(os.getenv("DATA_DIR", "data"))
        self.PROCESSED_DATA_DIR = os.path.join(self.DATA_DIR, "processed", "三国演义")
        self.VECTOR_STORE_DIR = os.path.join(self.DATA_DIR, "vector_store")

        ensure_directory(self.DATA_DIR)
        ensure_directory(self.VECTOR_STORE_DIR)

    def __str__(self):
        return f"Settings: {self.__dict__}"

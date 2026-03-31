import os
import sys
import unittest

# 添加 src 目录到 Python 路径
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from dotenv import load_dotenv

from sanguoagent.indexer import create_index, load_index, save_index
from sanguoagent.query_engine import get_query_engine, query_agent
from sanguoagent.settings import Settings
from sanguoagent.utils import ensure_directory

settings = Settings()


class TestQuery(unittest.TestCase):
    """测试查询功能"""

    @classmethod
    def setUpClass(cls):
        """设置测试环境"""
        load_dotenv()
        cls.data_dir = settings.PROCESSED_DATA_DIR
        cls.vector_store_dir = settings.VECTOR_STORE_DIR
        ensure_directory(cls.data_dir)
        ensure_directory(cls.vector_store_dir)

        # 构建或加载索引
        if (
            not os.path.exists(cls.vector_store_dir)
            or len(os.listdir(cls.vector_store_dir)) == 0
        ):
            cls.index = create_index(cls.data_dir)
            save_index(cls.index, cls.vector_store_dir)
        else:
            cls.index = load_index(cls.vector_store_dir)

        cls.query_engine = get_query_engine(cls.index)

    def test_basic_query(self):
        """测试基本查询功能"""
        question = "刘备是谁？"
        response = query_agent(self.query_engine, question)
        self.assertIsNotNone(response)
        self.assertIn("刘备", str(response))

    def test_complex_query(self):
        """测试复杂查询功能"""
        question = "赤壁之战的主要参与者有哪些？"
        response = query_agent(self.query_engine, question)
        self.assertIsNotNone(response)
        self.assertIn("赤壁之战", str(response))


if __name__ == "__main__":
    unittest.main()
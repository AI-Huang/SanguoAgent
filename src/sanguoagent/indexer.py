from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI

from .settings import Settings

settings = Settings()

llm = OpenAI(
    model=settings.MODEL,
    api_key=settings.OPENAI_API_KEY,
    api_base=getattr(settings, "OPENAI_API_BASE", None),
)


def create_index(data_dir=settings.PROCESSED_DATA_DIR):
    """创建向量索引"""
    # 加载文档
    documents = SimpleDirectoryReader(data_dir).load_data()

    # 创建索引，直接传递参数
    index = VectorStoreIndex.from_documents(
        documents,
        llm=llm,
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
    )

    return index


def save_index(index, save_path=settings.VECTOR_STORE_DIR):
    """保存索引"""
    index.storage_context.persist(persist_dir=save_path)


def load_index(load_path=settings.VECTOR_STORE_DIR):
    """加载索引"""
    from llama_index.core import StorageContext, load_index_from_storage

    storage_context = StorageContext.from_defaults(persist_dir=load_path)
    index = load_index_from_storage(storage_context)

    return index

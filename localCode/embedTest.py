from langchain_openai import OpenAIEmbeddings
embeddings_model = OpenAIEmbeddings()
embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh,hello",
        "What is your name?",
        "My friends call me World",
        "Hello World"
    ]
)
len(embeddings),len(embeddings[0])
#输出(5,1536)

# 通过 embed_query 查询坐标

query_embedding = embeddings_model.embed_query("What is the meaning of life?")
print(query_embedding)

##进行坐标缓存

from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

underlying_embeddings = OpenAIEmbeddings()

store  = LocalFileStore("/tmp/langchain_cache")

cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings,store,namespace=underlying_embeddings.model
)

list(store.yield_keys())

raw_documents = TextLoader("meow.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
# 创建向量存储 耗时2.58s
db = FAISS.from_documents(documents,cached_embedder)

#再次创建将读取缓存，从而加快速度降低成本 耗时2.49ms
db2 = FAISS.from_documents(documents,cached_embedder)

list(store.yield_keys())[:5]

##使用国产嵌入模型
##模型地址https://cloud.siliconflow.cn/models?type=embedding
from langchain_openai import OpenAIEmbeddings
import os
embeddings_model = OpenAIEmbeddings(
    model="BAAI/bge-m3",
    api_key="",
    base_url=""+'/v1'
)

embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh,hello",
        "What is your name?",
        "My friends call me World",
        "Hello World"
    ]
)

len(embeddings),len(embeddings[0])
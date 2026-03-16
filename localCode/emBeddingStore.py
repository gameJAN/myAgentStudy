from langchain_openai import OpenAIEmbeddings
import os
embeddings_model = OpenAIEmbeddings(
    model="BAAI/bge-m3",
    api_key="",
    base_url=""+'/v1'
)

from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embedding=embeddings_model)

from langchain_core.documents import Document
doucment_1 = Document(
    page_content="今天在抖音学会了一个新菜：锅巴土豆泥！看起来简单，实则炸了厨房，连猫都嫌弃地走开了",
    metadata={"source":"社交媒体"}
)

document_2=Document(
    page_content="小区遛狗大爷今日播报：广场舞大妈占领健身区，遛狗群众纷纷撤退。现场气氛诡异。",
    metadata={"source":"社区新闻"}
)

documents = [doucment_1,document_2]
# 添加基本索引 ['dc8dc496-8662-4f9b-bc4a-30ecfb15b029','1elaf831-abec-435f-b62e-529c69efc009']
vector_store.add_documents(documents=documents)

#也可以添加ID索引，便于后面管理 ["doc1","doc2"]
vector_store.add_documents(documents=documents,ids=["doc1",'doc2'])

#删除
vector_store.delete(ids=["doc1"])

# 查询
query="遛狗"
docs = vector_store.similarity_search(query)
print(docs[0].page_content)

#还可以用查相似向量地方式来查询
embedding_vector =  embeddings_model.embed_query(query)
docs=vector_store.similarity_search_by_vector(embedding_vector)
print(docs[0].page_content)


#mmr
vector_store.max_marginal_relevance_search(
    query="手机",
    k=1,
    lambda_val=0.8,
    filter={"source":"website"}
)

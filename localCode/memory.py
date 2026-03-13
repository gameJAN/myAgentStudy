# 增加链的记忆能力
# 短时记忆：InMemoryHistory
# 长时记忆 RunableWithMessageHistory

from typing import List
from pydantic import BaseModel,Field
from langchain_core.chat_history import BaseChatMessageHistory

from langchain_core.messages import BaseMessage,AIMessage

# 测试短时记忆
class InMemoryHistory(BaseChatMessageHistory,BaseModel):
    """内存中实现的聊天消息历史"""
    
    messages:list[BaseMessage] = Field(default_factory = list)

    def add_message(self, message:List[BaseModel]) ->None:
        """添加一组消息到存储中"""
        self.messages.extend(message)
    
    def clear(self)->None:
        """清空所有消息"""
        self.messages = []

store = {}

def get_by_session_id(session_id:str)->BaseChatMessageHistory:
    """根据会话ID获取历史记录，如果不存在则创建新的"""
    if session_id not in store:
        store[session_id] = InMemoryHistory()
    return store[session_id]

history = get_by_session_id("1")

history.add_message(AIMessage(content="你好"))

print(store)

# ----------------------------------------------------------
# 将记忆放到链里面

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    temperature=0,
    model="",
    api_key="",
    api_base=""
)

prompt = ChatPromptTemplate.from_messages([
    ("system","你是一个擅长{ability}的助手"),
    MessagesPlaceholder(variable_name="history"),
    ("human","{question}")
])

chain = prompt | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_by_session_id,
    input_messages_key="question",
    history_messages_key="history"
)

print(chain_with_history.invoke(
    {"ability":"math","question":"余弦函数是什么意思？"},
    config={"configurable":{"session_id":"foo"}}
))
print(chain_with_history.invoke(
    {"ability":"math","question":"余弦函数是什么意思？"},
    config={"configurable":{"session_id":"1"}}
))

print(store)
        
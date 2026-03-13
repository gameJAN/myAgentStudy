# 将对话记录存储在redis中形成长期记忆
import os
REDIS_URL =""
print(f"content to redis at:{REDIS_URL}")

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_redis import RedisChatMessageHistory
from langchain_deepseek import ChatDeepSeek
import os


llm = ChatDeepSeek(
    temperature=0,
    model="",
    api_key="",
    api_base=""
)

# 简单使用
history = RedisChatMessageHistory(session_id="user_123",redis_url=REDIS_URL)
history.clear()
history.add_user_message("你好，AI助手！")
history.add_ai_message("你好！我今天能为你提供什么帮助？")

print("聊天历史：")
for message in history.message:
    print(f"{type(message).__name__}:{message.content}")
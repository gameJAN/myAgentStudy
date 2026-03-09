
# 对话模板应用

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个起名大师，你的名字叫{name}."),
        ("human","你好{name},你感觉如何?"),
        ("ai","你好！我的状态非常好"),
        ("human","你叫什么名字"),
        ("ai","你好，我叫{name}"),
        ("human","{user_input}")
        
    ]
)

chats = chat_template.format_messages(name='成大事',user_input="你爸爸是谁呢?")
print(chats)
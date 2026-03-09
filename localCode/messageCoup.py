# 测试消息组合

from langchain_core.messages import  SystemMessage,HumanMessage,AIMessage

sy=SystemMessage(
    content="你是一个起名大师",
    additional_kwargs={"大师名字":"陈瞎子"}
)
hm=HumanMessage(content="请问大师叫什么")

ai=AIMessage(content="我叫陈瞎子")
[sy,hm,ai]
print(sy,hm,ai)

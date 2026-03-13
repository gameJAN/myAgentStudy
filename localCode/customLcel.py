from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os
from langchain_deepseek import ChatDeepSeek

claudeLLM = ChatDeepSeek(
    temperature=0,
    model="",
    api_key="",
    api_base=""
)

chain = (
    PromptTemplate.from_template(
        """根据下面的用户问题，将其分类为`LangChain`、`Anthropic`或`Other`
请只回复一个词作为答案

<question>
{question}
</question>

分类结果："""
    ) 
    |claudeLLM
    | StrOutputParser()
)

langchain_chain = PromptTemplate.from_template(
    """你将扮演一位LangChain专家。请以他的视角回答问题。 \
你的回答必须以"正如Harrison Chase告诉我的"开头，否则你会收到惩罚。\
请回答以下问题：

问题：{question}
回答："""
) | claudeLLM 

def test(x):
    print(x)



authropic_chain = PromptTemplate.from_template(
    """你将扮演一位Anthropic专家。请以他的视角回答问题。 \
你的回答必须以"正如Dario Amodei告诉我的"开头，否则你会收到惩罚。\
请回答以下问题：

问题：{question}
回答："""
) | claudeLLM  | RunnableLambda(test)


general_chain = PromptTemplate.from_template(
    """
请回答以下问题：

问题：{question}
回答："""
) | claudeLLM  

def route(info):
    print(info)
    if "anthropic" in info["topic"].lower():
        print("claude")
        return authropic_chain.invoke(info)
    elif "langchain" in info["topic"].lower():
        print("langchain")
        return langchain_chain.invoke(info)
    else:
        print("general")
        return general_chain.invoke(info)
    

full_chain = {"topic":chain,"question":lambda x:x["question"]} | RunnableLambda(route)

full_chain.invoke({"question":"我该如何使用claude？"})
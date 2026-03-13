# 将自己的方法变成lcel方法
from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_deepseek import ChatDeepSeek
import os

model = ChatDeepSeek(
    temperature=0,
    model="",
    api_key="",
    api_base=""
)

def length_function(text):
    return len(text)

def _mutiple_length_function(text1,text2):
    return len(text1) * len(text2)

def mutipile_length_function(_dict):
    return _mutiple_length_function(_dict['text1'],_dict["text2"])

prompt= ChatPromptTemplate.from_template("what is {a} + {b}")

chain=(
    {
        "a":itemgetter("foo") | RunnableLambda(length_function),
        "b":{"text1":itemgetter("foo"),"text2":itemgetter("bar")}|RunnableLambda(mutipile_length_function)
        |prompt | model
    }
)

chain.invoke({"foo":"bar","bar":"gah"})
from typing import Iterable,List
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek
llm = ChatDeepSeek(
    temperature=0,
    model="",
    api_key="",
    api_base=""
)

prompt = ChatPromptTemplate.from_template(
    "请列出5个与以下动物相似的动物名称，用逗号分隔：{animal}。不要包含数字"
)
str_chain = prompt | llm | StrOutputParser

for chunk in str_chain.stream({"animal":"熊"}):
    print(chunk,end="",flush=True)
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


# 自定义解析器，将LLM输出的标记迭代器
def split_into_list(input:Iterator[str]) -> Iterator[List[str]]:
    buffer = ""
    for chunk in input:
        buffer += chunk
        while "," in buffer:
            comma_index = buffer.index(",")
            yield [buffer[:comma_index].strip()]
            buffer = buffer[comma_index + 1:]

    yield [buffer.strip()]


list_chain = str_chain | split_into_list

for chunk in list_chain.stream({"animal":"熊"}):
    print(chunk,flush=True)

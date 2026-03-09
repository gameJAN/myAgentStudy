from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=""
)
llm.invoke('介绍你自己')
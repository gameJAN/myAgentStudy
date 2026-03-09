# 测试自定义模板应用
from langchain_core.prompts import StringPromptTemplate

def hello_world(abc):
    print("Hello world")
    return abc

PROMPT = """
你是一个非常有经验和天赋的程序员，现在给你如下函数名，你会按照如下格式，输出这段代码的名称、源代码、中文解释。
函数名词:{function_name}
源代码:
{source_code}
代码解释:
"""

import inspect

def get_source_code(function_name):
    return inspect.getsource(function_name)

class customPrompt(StringPromptTemplate):
    def format(self,**kwargs)-> str:
        source_code = get_source_code(kwargs["function_name"])
        
        prompt =PROMPT.format(
            function_name = kwargs["function_name"].__name__,source_code=source_code
        )
        return prompt

# 使用自定义提示词模板
a = customPrompt(input_variables=["function_name"])

pm = a.format(function_name = hello_world)

print(pm)

# 链接LLM

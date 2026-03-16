# 自定义一个文件加载器
from typing import AsyncIterator,Iterator

# 目前市面上的文件loader都继承自BaseLoader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

class CustomDocumentLoader(BaseLoader):
    """逐行读取文件的文档加载器示例"""

    def __init__(self,file_path: str) -> None:

        self.file_path = file_path

    def lazy_load(self) ->Iterator[Document]:
        """逐行读取文件的惰性加载器
            当实现惰性加载方式的时候，应该用生成器一次生成一个文档
        """
        with open(self.file_path,encoding="utf-8") as f:
            line_number = 0
            for line in f:
                yield Document(
                    page_content=line,
                    metadata={"line_number":line_number,"source":self.file_path},
                )
                line_number+=1
        
    async def alazy_load(self)-> AsyncIterator[Document]:
        import aiofiles

        async with aiofiles.open(self.file_path,encoding="utf-8") as f:
            line_number = 0
            for line in f:
                yield Document(
                    page_content=line,
                    metadata={"line_number":line_number,"source":self.file_path},
                )
                line_number+=1

from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.callbacks.manager import CallbackManagerForRetrieverRun
from typing import List
from langchain.schema import Document
import time


class RateLimitedMultiQueryRetriever(MultiQueryRetriever):
    """在每次查询之间加入延迟，避免触发限流"""
    request_delay: float = 0.8  # 每条查询间隔秒数

    def _get_relevant_documents(
            self,
            query: str,
            *,
            run_manager: CallbackManagerForRetrieverRun,
    ) -> List[Document]:
        # 生成多条查询
        queries = self.generate_queries(query, run_manager)

        # 串行检索，每次之间等待
        documents = []
        for q in queries:
            docs = self.retriever.get_relevant_documents(q)
            documents.extend(docs)
            time.sleep(self.request_delay)  # 限速

        # 去重
        return self.unique_union(documents)
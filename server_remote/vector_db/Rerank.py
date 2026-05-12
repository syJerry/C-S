from typing import List

import requests
from exceptiongroup import catch
from langchain_core.documents import Document
from logzero import logger
from sentence_transformers import CrossEncoder
from model_util.Model import reranker


class Rerank:
    @staticmethod
    def _cross_encoder_rerank_local(query: str, docs: List[Document], reranker=reranker):

        pairs = [(query, doc.page_content) for doc in docs]
        scores = reranker.predict(pairs, show_progress_bar=False)

        scored_docs = sorted(
            zip(scores, docs),
            key=lambda x: x[0],
            reverse=True,
        )

        # 把分数写回 metadata，方便调试
        result = []
        for score, doc in scored_docs:
            doc.metadata["rerank_score"] = round(float(score), 4)
            result.append(doc)
        return result

    @staticmethod
    def cross_encoder_rerank(query: str, docs: List[Document]) -> List[Document]:
        # if not docs:
        #     return []
        # logger.info("发送网络请求> localhost:43421")
        # url = f"http://127.0.0.1:43421/rerank"
        # payload = {
        #     "query": query,
        #     "docs": [
        #         {
        #             "page_content": doc.page_content,
        #             "metadata": doc.metadata,
        #         }
        #         for doc in docs
        #     ],
        # }
        # reranked_docs = []

        # try:
        #     response = requests.post(url, json=payload)
        #     response.raise_for_status()
        #     results = response.json()["docs"]
        #     logger.info(f"收到服务器回复，有{len(results)}条数据！")
        #     for d in results:
        #         reranked_docs.append(
        #             Document(
        #                 page_content=d["page_content"],
        #                 metadata=d.get("metadata", {}),
        #             )
        #         )
        # except:
        #     logger.info("网络错误，开始本地重排序！")
            # reranked_docs = Rerank._cross_encoder_rerank_local(query, docs)
        reranked_docs = Rerank._cross_encoder_rerank_local(query, docs)

        return reranked_docs

    @staticmethod
    def rrf_rerank(
            vector_results: List[Document], bm25_results: List[Document]
    ) -> List[Document]:
        """RRF (Reciprocal Rank Fusion) 重排（备用）"""
        rrf_scores = {}
        k = 60

        for rank, doc in enumerate(vector_results):
            doc_id = id(doc)
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1 / (k + rank + 1)

        for rank, doc in enumerate(bm25_results):
            doc_id = id(doc)
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1 / (k + rank + 1)

        all_docs = {id(doc): doc for doc in vector_results + bm25_results}
        sorted_docs = sorted(
            all_docs.items(),
            key=lambda x: rrf_scores.get(x[0], 0),
            reverse=True,
        )
        return [doc for _, doc in sorted_docs]

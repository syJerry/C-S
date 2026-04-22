import re
from typing import List

import jieba
from langchain.chains.llm import LLMChain
from langchain.schema import Document
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseLanguageModel
from langchain_core.output_parsers import BaseOutputParser
from logzero import logger

from model_util.Model import llm
from model_util.Prompt import QUERY_PROMPT
from vector_db.Compress import Compress
from vector_db.RateLimitedMultiQueryRetriever import RateLimitedMultiQueryRetriever
from vector_db.Rerank import Rerank


def _chinese_tokenizer(text):
    return list(jieba.cut(text))


def _print_docs(list_of_docs):
    for doc in list_of_docs:
        logger.info("%s", doc.page_content)


class HyDEMultiQueryParser(BaseOutputParser[List[str]]):
    """
    解析融合了 HyDE 的多查询输出。
    返回所有查询（包括假设性文档片段），统一用于检索。
    """

    def parse(self, text: str) -> List[str]:
        queries = []
        extend_contents = []
        for line in text.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            # 去掉前缀标签（查询1:、假设文档: 等）
            cleaned = re.sub(r"^(查询\d+|假设文档)\s*[:：]\s*", "", line).strip()
            hyp_doc = re.sub(r"^假设文档\d*\s*[:：]\s*", "", line).strip()
            if cleaned:
                extend_contents.append(cleaned)
            if hyp_doc:
                queries.append(hyp_doc)
        print(f"=== 解析后共 {len(queries)} 条查询 ===")
        for i, q in enumerate(queries, 1):
            print(f"  [{i}] {q}")
        return queries


class Retriever:
    def __init__(self):
        self.vector_retriever_hyde = None
        self.title_retriever = None
        self.bm25_retriever = None
        # self.vector_store = None
        self.score_threshold = 0.5

        # 压缩器（需调用 setup_compressor 后才可用）
        self.compressor = None

        # 测试变量
        self.vector_retriever_hyde_test = None
        self.title_retriever_test = None
        self.bm25_retriever_test = None
        self.vector_retriever_test = None

    def setup_retriever(self, vectorstore: Chroma, titlestore: Chroma, document_data):
        """设置向量检索器和BM25检索器"""
        # self.vector_retriever = vectorstore.as_retriever(
        #     search_type="mmr",
        #     search_kwargs={'k': 20, 'lambda_mult': 0.25}
        # )
        self.vector_retriever_hyde = self.build_hyde_multi_query_retriever(vectorstore, llm)

        self.title_retriever = titlestore.as_retriever(
            search_type="mmr",
            search_kwargs={'k': 40, 'lambda_mult': 0.25}
        )
        self.bm25_retriever = BM25Retriever.from_documents(
            document_data.docs,
            k=20,
            preprocess_func=_chinese_tokenizer
        )
        # self.vector_store = vectorstore

    def setup_compressor(
            self,
            llm: BaseLanguageModel | None,
            embeddings: Embeddings | None,
            mode: str = "embedding",
            similarity_threshold: float = 0.4,
            chunk_size: int = 300,
    ):
        self.compressor = Compress.setup_compressor(llm, embeddings, mode, similarity_threshold, chunk_size)

    def search(self, query: str, top_k: int = 3) -> List[Document]:
        """
        混合检索入口。
        若已调用 setup_compressor，则在重排后自动执行压缩；否则直接返回重排结果。
        """
        docs = self._hybrid_search(query, top_k)

        if self.compressor is not None:
            docs = self._compress(query, docs)
        return docs

    def _compress(self, query: str, docs: List[Document]) -> List[Document]:
        """对重排后的文档执行压缩，过滤掉无关内容"""
        return Compress.compress(self.compressor, query, docs)

    def _hybrid_search(self, query: str, top_k: int) -> List[Document]:
        """混合检索 - 结合向量检索和BM25检索，使用 Cross-Encoder 重排"""
        try:
            titles_docs = self.title_retriever.invoke(query)
            vector_docs = self.vector_retriever_hyde.invoke(query)
        except:
            titles_docs = []
            vector_docs = []
        title_filter = self._process_titles(titles_docs)
        bm25_docs = self.bm25_retriever.get_relevant_documents(query)

        # 查询后手动过滤：breadcrumb 包含任意候选标题
        if title_filter:
            vector_docs = [
                doc for doc in vector_docs
                if any(c in doc.metadata.get("breadcrumb", "") for c in title_filter)
            ]

        logger.info("标题检索结果>")
        logger.info([f"检索到{len(titles_docs)}条标题"])
        logger.info("向量检索结果(过滤后)>")
        logger.info([f"检索到{len(vector_docs)}条向量"])
        logger.info("关键词检索结果>")
        logger.info([f"检索到{len(bm25_docs)}条关键词向量"])

        merged_docs = self._deduplicate(vector_docs + bm25_docs)
        logger.info(f"合并去重后候选数量: {len(merged_docs)}")

        reranked_docs = Rerank.cross_encoder_rerank(query, merged_docs)
        filter_docs = self.score_filter(reranked_docs)
        logger.info(f"合并去重后候选数量: {len(filter_docs)}")

        return filter_docs

    def build_hyde_multi_query_retriever(self, vectorstore, llm):
        # 用 LLMChain 替代 LCEL pipeline
        llm_chain = LLMChain(
            llm=llm,
            prompt=QUERY_PROMPT,
            output_parser=HyDEMultiQueryParser(),
        )

        retriever = RateLimitedMultiQueryRetriever(
            retriever=vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 5},
            ),
            llm_chain=llm_chain,
            # 不传 parser_key，让它用 output_parser 的结果
        )

        return retriever

    def score_filter(self, rerank_docs: list[Document]):
        res = []
        for i, doc in enumerate(rerank_docs):
            score = doc.metadata["rerank_score"]
            logger.info(f"[{i}]分数:{score}")
            if score >= self.score_threshold:
                res.append(doc)
        return res

    @staticmethod
    def _deduplicate(docs: List[Document]) -> List[Document]:
        seen, result = set(), []
        for doc in docs:
            if doc.page_content not in seen:
                seen.add(doc.page_content)
                result.append(doc)
        return result

    @staticmethod
    def _process_titles(titles_docs: List[Document]) -> List[str]:
        return [doc.page_content for doc in titles_docs]

    # ─────────────────────────────────────────────
    # 测试接口
    # ─────────────────────────────────────────────
    def setup_test(self, vectorstore: Chroma, titlestore: Chroma, document_data):
        self.vector_retriever_test = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={'k': 20, 'lambda_mult': 0.25}
        )
        self.vector_retriever_hyde_test = self.build_hyde_multi_query_retriever(vectorstore, llm)

        self.title_retriever_test = titlestore.as_retriever(
            search_type="mmr",
            search_kwargs={'k': 40, 'lambda_mult': 0.25}
        )
        self.bm25_retriever_test = BM25Retriever.from_documents(
            document_data.docs,
            k=20,
            preprocess_func=_chinese_tokenizer
        )

    def search_test(self, query: str, top_k: int, test_type="baseline"):
        if test_type == "baseline":
            vec_docs = self.vector_retriever_test.invoke(query)
            bm25_docs = self.bm25_retriever_test.get_relevant_documents(query)
            rerank_docs = Rerank.rrf_rerank(vec_docs, bm25_docs)
            merged_docs = self._deduplicate(rerank_docs)
            return merged_docs[:top_k]
        elif test_type == "e1":
            vec_docs = self.vector_retriever_hyde_test.invoke(query)
            bm25_docs = self.bm25_retriever_test.get_relevant_documents(query)
            rerank_docs = Rerank.rrf_rerank(vec_docs, bm25_docs)
            merged_docs = self._deduplicate(rerank_docs)
            return merged_docs[:top_k]
        elif test_type == "e2":
            titles_docs = self.title_retriever_test.invoke(query)
            vec_docs = self.vector_retriever_test.invoke(query)
            bm25_docs = self.bm25_retriever_test.get_relevant_documents(query)
            title_filter = self._process_titles(titles_docs)
            if title_filter:
                vec_docs = [
                    doc for doc in vec_docs
                    if any(c in doc.metadata.get("breadcrumb", "") for c in title_filter)
                ]
            merged_docs = self._deduplicate(vec_docs + bm25_docs)
            rerank_docs = Rerank.cross_encoder_rerank(query, merged_docs)
            return rerank_docs[:top_k]
        elif test_type == "e3":
            titles_docs = self.title_retriever_test.invoke(query)
            vec_docs = self.vector_retriever_test.invoke(query)
            bm25_docs = self.bm25_retriever_test.get_relevant_documents(query)
            title_filter = self._process_titles(titles_docs)
            if title_filter:
                vec_docs = [
                    doc for doc in vec_docs
                    if any(c in doc.metadata.get("breadcrumb", "") for c in title_filter)
                ]
            rerank_docs = Rerank.rrf_rerank(vec_docs,bm25_docs)
            merged_docs = self._deduplicate(rerank_docs)
            return merged_docs[:top_k]
        elif test_type=="e4":
            vec_docs = self.vector_retriever_hyde_test.invoke(query)
            bm25_docs = self.bm25_retriever_test.get_relevant_documents(query)
            merged_docs = self._deduplicate(vec_docs + bm25_docs)
            rerank_docs = Rerank.cross_encoder_rerank(query,merged_docs)
            return rerank_docs[:top_k]
        elif test_type=="full":
            vec_docs = self.vector_retriever_hyde_test.invoke(query)
            bm25_docs = self.bm25_retriever_test.get_relevant_documents(query)
            titles_docs = self.title_retriever_test.invoke(query)
            title_filter = self._process_titles(titles_docs)
            if title_filter:
                vec_docs = [
                    doc for doc in vec_docs
                    if any(c in doc.metadata.get("breadcrumb", "") for c in title_filter)
                ]
            merged_docs = self._deduplicate(vec_docs + bm25_docs)
            rerank_docs = Rerank.cross_encoder_rerank(query,merged_docs)
            return rerank_docs[:top_k]


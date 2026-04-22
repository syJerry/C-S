from typing import List

from langchain.retrievers.document_compressors import (
    LLMChainExtractor,
    EmbeddingsFilter,
    DocumentCompressorPipeline,
)
from langchain.schema import Document
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseLanguageModel
from langchain_text_splitters import CharacterTextSplitter
from logzero import logger

from model_util import Prompt


class Compress:
    @staticmethod
    def setup_compressor(
            llm: BaseLanguageModel | None,
            embeddings: Embeddings | None,
            mode: str = "embedding",
            similarity_threshold: float = 0.4,
            chunk_size: int = 300,
    ):
        """
        初始化文档压缩器。

        Args:
            llm: 用于 LLMChainExtractor 的语言模型
            embeddings: 用于 EmbeddingsFilter 的嵌入模型
            mode: 压缩模式
                - "llm"       LLM 精抽取，精度最高，消耗 token
                - "embedding" Embedding 相似度过滤，速度快，不消耗 token
                - "pipeline"  先过滤再抽取，平衡精度与速度（推荐）
            similarity_threshold: EmbeddingsFilter 的相似度阈值（0~1）
            chunk_size: Pipeline 模式下切句的粒度（字符数）
        """
        if mode == "llm":
            compressor = LLMChainExtractor.from_llm(
                llm, prompt=Prompt.CN_EXTRACT_PROMPT
            )

        elif mode == "embedding":
            compressor = EmbeddingsFilter(
                embeddings=embeddings,
                similarity_threshold=similarity_threshold,
            )

        elif mode == "pipeline":
            splitter = CharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=0,
                separator="。",
            )
            embeddings_filter = EmbeddingsFilter(
                embeddings=embeddings,
                similarity_threshold=similarity_threshold,
            )
            llm_extractor = LLMChainExtractor.from_llm(
                llm, prompt=Prompt.CN_EXTRACT_PROMPT
            )
            compressor = DocumentCompressorPipeline(
                transformers=[splitter, embeddings_filter, llm_extractor]
            )

        else:
            raise ValueError(f"不支持的压缩模式: {mode}，可选值为 llm / embedding / pipeline")

        logger.info(f"已初始化压缩器，模式: {mode}")
        return compressor

    @staticmethod
    def compress(compressor,query: str, docs: List[Document]) -> List[Document]:
        """对重排后的文档执行压缩，过滤掉无关内容"""
        if not docs:
            return []

        compressed = compressor.compress_documents(docs, query)

        logger.info(f"压缩前文档数: {len(docs)}，压缩后文档数: {len(compressed)}")
        logger.info("压缩后结果>")

        return list(compressed)

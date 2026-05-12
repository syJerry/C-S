import os
from typing import List

import dill
import jieba
import tqdm
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from logzero import logger

from config.load import json_config
from model_util.Model import embedding
from vector_db.DataPreparation import DataPreparation
from vector_db.MarkdownParse import Markdown
from vector_db.Retriever import Retriever
from vector_db.util.Chunk import HeadingNode

CONTENT_COLLECT = "CONTENT_COLLECT"
TITLE_COLLECT = "TITLE_COLLECT"


def chinese_tokenizer(text):
    return list(jieba.cut(text))


def _print_docs(list_of_docs):
    for doc in list_of_docs:
        logger.info("%s", doc.page_content)


class VectorDB:
    def __init__(self, persist_dir: str, embedding_batch: int):

        self.retriever = Retriever()
        self.persist_dir = persist_dir
        self.vectorstore: Chroma | None = None
        self.titlestore: Chroma | None = None
        self.document_data: Markdown | None = None
        self.embedding_batch = embedding_batch

    def save(self):
        os.makedirs(self.persist_dir, exist_ok=True)
        if self.vectorstore:
            self.vectorstore.persist()  # 确保持久化
        if self.titlestore:
            self.titlestore.persist()
        if self.document_data:
            with open(os.path.join(self.persist_dir, "markdown.pkl"), "wb") as f:
                dill.dump(self.document_data, f)
        logger.info(f"已保存到 {self.persist_dir}")

    def loadDB(self, document_data: Markdown):
        if os.path.exists(self.persist_dir):
            self.vectorstore = Chroma(
                collection_name=CONTENT_COLLECT,
                persist_directory=self.persist_dir,
                embedding_function=embedding,
            )
            self.titlestore = Chroma(
                collection_name=TITLE_COLLECT,
                persist_directory=self.persist_dir,
                embedding_function=embedding,
            )
            count = self.vectorstore._collection.count()
            logger.info(f"加载完成，共 {count} 条内容向量")
            if count == 0:
                logger.warning("向量库为空！请删除持久化目录后重新 buildDB")
            count = self.titlestore._collection.count()
            logger.info(f"加载完成，共 {count} 条标题向量")
            if count == 0:
                logger.warning("向量库为空！请删除持久化目录后重新 buildDB")
        else:
            raise FileNotFoundError(f"持久化目录不存在: {self.persist_dir}")
        self.document_data = document_data
        self.setup_retrievers()

    def build_doc(self, path: str):
        if os.path.isfile(path):
            self.document_data = DataPreparation.loadPDF(path)
        elif os.path.isdir(path):
            self.document_data = DataPreparation.loadData(path)
    

    def buildDB(self):
        self.build_doc(json_config['data'].get("raw_data"))
        if not self.document_data or not self.document_data.docs:
            raise ValueError("文档加载失败或为空")

        self.vectorstore = Chroma(
            collection_name=CONTENT_COLLECT,
            embedding_function=embedding,
            persist_directory=self.persist_dir,
        )
        self.titlestore = Chroma(
            collection_name=TITLE_COLLECT,
            embedding_function=embedding,
            persist_directory=self.persist_dir,
        )

        for i in tqdm.tqdm(range(0, len(self.document_data.docs), self.embedding_batch), "创建内容向量库"):
            batch = self.document_data.docs[i:i + self.embedding_batch]
            self.vectorstore.add_documents(batch)
            self.vectorstore.persist()

        for i in tqdm.tqdm(range(0, len(self.document_data.titles), self.embedding_batch), "创建标题向量库"):
            batch = self.document_data.titles[i:i + self.embedding_batch]
            self.titlestore.add_texts(batch)
            self.titlestore.persist()
        self.save()
        self.setup_retrievers()
        logger.info(f"buildDB 完成，共写入 {self.vectorstore._collection.count()} 条内容向量")
        logger.info(f"buildDB 完成，共写入 {self.titlestore._collection.count()} 条标题向量")

    def setup_retrievers(self):
        self.retriever.setup_retriever(self.vectorstore, self.titlestore, self.document_data)
        # self.retriever.setup_compressor(llm=None,embeddings=embedding)

    def post_process(self, search_res: List[Document]) -> List[Document]:
        """
        重新组织结果，包括去重，组织整个标题内容，恢复markdown格式
        :param search_res: 初步查询结果
        :return:
        """
        nodup = self.remove_duplicate(search_res)
        logger.info(f"去重后结果{len(nodup)}")
        layout_res = self.recover_layout(nodup)
        logger.info(f"恢复布局后结果{len(layout_res)}")

        return layout_res

    @staticmethod
    def remove_duplicate(search_res: List[Document]) -> List[Document]:
        seen_ids = set()
        unique_docs = []

        for doc in search_res:
            doc_id = doc.metadata.get("chunk_id")
            if doc_id not in seen_ids:
                seen_ids.add(doc_id)
                unique_docs.append(doc)

        return unique_docs

    def recover_layout(self, nodup_res: List[Document]) -> List[Document]:
        layout_docs = []
        heads_set: set[str] = set()
        for doc in nodup_res:
            id = doc.metadata.get("chunk_id")
            chunk_index = self.document_data.chunks_map[id]
            chunk = self.document_data.chunks[chunk_index]
            assert doc.page_content == chunk.content
            node = chunk.heading
            s = HeadingNode.to_markdown(node, heads_set)
            layout_docs.append(Document(page_content=s))
        return layout_docs

    def queryDB(self, query: str, k) -> List[Document]:
        if self.vectorstore is None:
            raise RuntimeError("数据库尚未构建，请先调用buildDB()")

        total = self.vectorstore._collection.count()
        logger.info(f"查询: '{query}' | k={k}, 库总量={total}")

        res = self.retriever.search(query, k)
        post_res = self.post_process(res)
        logger.info(f"后处理有{len(post_res)}条")
        _print_docs(post_res)
        return post_res

    def test(self):
        logger.info("=" * 60)
        logger.info(f"数据库数据量: {self.vectorstore._collection.count()}")
        logger.info(f"文档块数：{self.document_data.chunk_count}")
        logger.info("=" * 60)
        embeddings = embedding.embed_documents(
            [doc.page_content for doc in self.document_data.docs[:3]]
        )
        for i, emb in enumerate(embeddings):
            print(i, emb[:5])

        # 测试
        # self.document_data.show()
        # print(self.document_data.is_clustered())

    def setup_test(self):
        self.retriever.setup_test(self.vectorstore, self.titlestore, self.document_data)

    def queryDB_test(self, query: str, k, test_type: str):
        res = self.retriever.search_test(query, k, test_type)
        post_res = self.post_process(res)
        return post_res


def make_chromaDB():
    persist_dir = json_config["vectorDB"].get("persist_dir")
    embedding_batch = json_config["vectorDB"].get("embedding_batch")
    new_db = VectorDB(persist_dir, embedding_batch)

    md_path = os.path.join(persist_dir, "markdown.pkl")

    if os.path.exists(persist_dir):
        logger.info("正在加载 vectorDB")

        if not os.path.exists(md_path):
            raise FileNotFoundError(f"找不到 {md_path}，请重新 buildDB")
        with open(md_path, "rb") as f:
            md: Markdown = dill.load(f)
        new_db.loadDB(md)
    else:
        logger.info("正在创建 vectorDB")
        new_db.buildDB()

    return new_db


db = make_chromaDB()

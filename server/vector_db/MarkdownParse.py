import logzero
from typing import Dict

from langchain_core.documents import Document
from tqdm import tqdm

from vector_db.util.Chunk import HeadingNode, Chunk
from vector_db.util.Parse import _parse_md_to_chunks


class Markdown:
    def __init__(self, docs, chunks, titles, chunks_map, chunk_count):
        self.docs: list[Document] = docs
        self.chunks: list[Chunk] = chunks
        self.chunks_map: Dict[str, int] = chunks_map
        self.chunk_count: int = chunk_count
        self.titles = titles
        self.is_merge = False

        if not self.is_merge:
            self.merge()

        logzero.logger.info("*" * 60)
        logzero.logger.info(f"共解析得到{len(self.docs)}个documents!")
        logzero.logger.info(f"共解析得到{len(self.chunks)}chunks!")
        logzero.logger.info(f"共解析得到{len(self.titles)}titles!")
        logzero.logger.info("*" * 60)

    def merge(self):
        logzero.logger.info("正在合并分块!")
        self.is_merge = True
        prev: None | Chunk = None
        new_chunks: list[Chunk] = []
        new_map: Dict[str, int] = {}
        new_docs: list[Document] = []
        new_count = 0
        for chunk in tqdm(self.chunks, "合并chunk"):
            if not prev:
                prev = chunk
                continue
            if chunk.heading.id != prev.heading.id:
                new_chunks.append(prev)
                new_map[prev.id] = new_count
                new_count += 1
                new_docs.append(prev.to_document())
                prev = chunk
                continue
            prev.content += chunk.content
        self.docs = new_docs
        self.chunks = new_chunks
        self.chunks_map = new_map
        self.chunk_count = new_count
        assert len(new_docs) == new_count
        logzero.logger.info(f"合并完成，共有{new_count}块")

    def show(self):
        html_content = """
        <html>
        <head>
        <meta charset="utf-8">
        <title>Documents</title>
        </head>
        <body style="font-family: Arial;">
        <h2>Document Viewer</h2>
        """
        for i, doc in enumerate(self.docs):
            color = "#f6f6f6" if i % 2 == 0 else "#ffffff"

            html_content += f"""
            <div style="
                background-color:{color};
                padding:15px;
                margin:10px 0;
                border-radius:8px;
                border:1px solid #ddd;
            ">
                <div style="white-space: pre-wrap;">
                {doc.page_content}
                </div>
            </div>
            """

        html_content += "</body></html>"

        with open("docs_view2.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        print("已生成 docs_view.html")

    def is_clustered(self):
        seen = set()
        prev = None
        for chunk in self.chunks:
            str = chunk.heading.id
            if str != prev:
                if str in seen:
                    return False
                seen.add(str)
            prev = str
        return True


class MarkdownParse:
    @staticmethod
    def parse_markdown(
            md_text: str,
            source_file: str = "",
    ) -> tuple[HeadingNode, list[Chunk]]:
        """
        解析单个 Markdown 字符串，返回标题树根节点和所有 Chunk。

        Args:
            md_text     : Markdown 原文
            source_file : 可选的来源标识（文件名、URL 等）

        Returns:
            (root, chunks)
        """
        return _parse_md_to_chunks(md_text, source_file=source_file)

    @staticmethod
    def build_documents(
            md_texts: list[str],
            source_files: list[str] | None = None,
    ) -> list[Document]:
        """
        批量处理多个 Markdown 字符串，返回可直接用于 embedding 的
        LangChain Document 列表。

        Args:
            md_texts     : Markdown 字符串列表（即题目中的 [str, ...]）
            source_files : 与 md_texts 等长的来源标识列表（可选）

        Returns:
            List[Document]  每个 Document 的 metadata 包含：
                - chunk_id            本块 UUID
                - source_file         来源文件标识
                - heading_title       所属标题文字
                - heading_level       所属标题级别（1–6，根节点为 0）
                - heading_id          所属标题 UUID
                - breadcrumb          "根 > 父 > 当前" 路径字符串
                - parent_heading_title 父标题文字（无父时为 None）
                - parent_heading_id   父标题 UUID（无父时为 None）
                - child_heading_ids   子级标题 UUID 列表（一层）
                - child_chunk_ids     子级标题下所有切块 UUID（递归）
                - sibling_chunk_ids   同级（兄弟）切块 UUID 列表
        """
        if source_files is None:
            source_files = [f"doc_{i}" for i in range(len(md_texts))]

        all_docs: list[Document] = []
        for text, src in zip(md_texts, source_files):
            _, chunks = _parse_md_to_chunks(text, source_file=src)
            all_docs.extend(chunk.to_document() for chunk in chunks)

        return all_docs

    @staticmethod
    def Parse2Markdown(
            md_texts: list[str],
            source_files: list[str] | None = None,
    ) -> Markdown:
        """

        :param md_texts:
        :param source_files:
        :return:
        """
        if source_files is None:
            source_files = [f"doc_{i}" for i in range(len(md_texts))]

        chunk_map = {}
        all_docs = []
        all_chunks = []
        titles = []
        for text, src in zip(md_texts, source_files):
            root, chunks = _parse_md_to_chunks(text, source_file=src)
            all_docs.extend(chunk.to_document() for chunk in chunks)
            all_chunks += chunks
            titles.extend(HeadingNode.collect_all_titles(root))

        for i, chunk in enumerate(all_chunks):
            chunk_map[chunk.id] = i

        return Markdown(all_docs, all_chunks,titles, chunk_map, len(all_chunks))

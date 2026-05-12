from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Optional

from langchain_core.documents import Document




@dataclass
class HeadingNode:
    """
    Markdown 标题树中的一个节点。

    Attributes:
        id          全局唯一 ID（UUID）
        level       标题级别（1–6）
        title       标题文字（不含 # 前缀）
        parent      父节点（None 表示根）
        children    子节点列表（HeadingNode）
        chunks      直属于本节点的 Chunk 列表
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    level: int = 0
    title: str = ""
    parent: Optional["HeadingNode"] = field(default=None, repr=False)
    children: list["HeadingNode"] = field(default_factory=list, repr=False)
    chunks: list["Chunk"] = field(default_factory=list, repr=False)

    @property
    def heading_path(self) -> list[str]:
        """从根到自身的标题路径，例如 ['H1', 'H2', '当前标题']"""
        node, path = self, []
        while node and node.level > 0:
            path.append(node.title)
            node = node.parent
        return list(reversed(path))

    @property
    def breadcrumb(self) -> str:
        """[根标题 ,子标题 ,当前标题]"""
        return " > ".join(self.heading_path)
        # return self.heading_path

    @staticmethod
    def to_markdown(node: HeadingNode, heads_set: set[str]) -> str:
        s = ""
        if node.id in heads_set:
            return s
        heads_set.add(node.id)
        if node.level > 0:
            s += "#" * node.level + " " + node.title + "\n\n"
        for chunk in node.chunks:
            s += chunk.content + "\n\n"
        for child in node.children:
            s += HeadingNode.to_markdown(child, heads_set)
        return s

    @staticmethod
    def collect_all_titles(node:HeadingNode):
        return _collect_all_titles(node)

@dataclass
class Chunk:
    """
    一个内容块（对应 Markdown 中的一个段落或代码块等）。

    Attributes:
        id          全局唯一 ID
        content     原始文本内容
        heading     所属 HeadingNode
        source_file 来源文件标识（可选）
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content: str = ""
    heading: HeadingNode = field(default_factory=HeadingNode, repr=False)
    source_file: str = ""

    @property
    def parent_heading(self) -> Optional[HeadingNode]:
        """直接父标题节点（即 self.heading 本身的 parent）"""
        return self.heading.parent

    @property
    def sibling_chunks(self) -> list["Chunk"]:
        """与本块在同一标题下的所有切块（含自身）"""
        return list(self.heading.chunks)

    @property
    def child_chunks(self) -> list["Chunk"]:
        """
        本块所属标题下所有子级标题的全部切块
        （递归收集，对应"当前标题的子级标题的所有切块"需求）
        """
        result: list[Chunk] = []
        for child_heading in self.heading.children:
            result.extend(_collect_all_chunks(child_heading))
        return result

    def to_document(self) -> Document:
        """转换为 LangChain Document，metadata 包含完整层级信息。"""
        meta = {
            "chunk_id": self.id,
            "source_file": self.source_file,
            # 当前所属标题
            "heading_title": self.heading.title,
            "heading_level": self.heading.level,
            "heading_id": self.heading.id,
            # 面包屑路径
            "breadcrumb": self.heading.breadcrumb,
            # 父标题
            "parent_heading_title": (
                self.heading.parent.title if self.heading.parent else None
            ),
            "parent_heading_id": (
                self.heading.parent.id if self.heading.parent else None
            ),
            # 子级标题 IDs（一层）
            # "child_heading_ids": [c.id for c in self.heading.children],
            # # 子级所有切块 IDs（递归）
            # "child_chunk_ids": [ch.id for ch in self.child_chunks],
            # # 同级切块 IDs
            # "sibling_chunk_ids": [ch.id for ch in self.sibling_chunks],
        }
        return Document(page_content=self.content, metadata=meta)

    # def to_markdown(self, output_title: bool) -> tuple[HeadingNode, str]:
    #     s = ""
    #     if output_title:
    #         tem_s = "#" * self.heading.level
    #         tem_s += " "
    #         tem_s += self.heading.title
    #         tem_s += "\n\n"
    #         s += tem_s
    #     s += self.content
    #     s += "\n\n"
    #     return self.heading, s


def _collect_all_chunks(node: HeadingNode) -> list[Chunk]:
    """递归收集节点及其所有子孙节点的全部切块。"""
    # result = list(node.chunks)
    result = _merge_chunks(node.chunks)
    for child in node.children:
        result.extend(_collect_all_chunks(child))
    return result


def _merge_chunks(chunks: list[Chunk]) -> list[Chunk]:
    new_chunk = chunks[0]
    for i in range(1, len(chunks)):
        new_chunk.content += chunks[i].content

    return [new_chunk]

def _collect_all_titles(node: HeadingNode)->list[str]:
    res = [node.title]
    for child in node.children:
        res.extend(_collect_all_titles(child))
    return res


import re

from vector_db.util.Chunk import HeadingNode, Chunk


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")

def _split_paragraphs(text: str) -> list[str]:
    """
    将文本按空行分割为段落。
    • 代码块（``` … ```）视为一个整体，不会被拆开。
    • 返回非空段落列表。
    """
    paragraphs: list[str] = []
    current_lines: list[str] = []
    in_code_block = False

    for line in text.split("\n"):
        stripped = line.strip()
        # 切换代码块状态
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
            current_lines.append(line)
            continue

        if in_code_block:
            current_lines.append(line)
            continue

        if stripped == "":
            # 空行 → 段落分隔
            if current_lines:
                para = "\n".join(current_lines).strip()
                if para:
                    paragraphs.append(para)
                current_lines = []
        else:
            current_lines.append(line)

    # 收尾
    if current_lines:
        para = "\n".join(current_lines).strip()
        if para:
            paragraphs.append(para)

    return paragraphs

def _parse_md_to_chunks(
    md_text: str,
    source_file: str = "",
) -> tuple[HeadingNode, list[Chunk]]:
    """
    解析单个 Markdown 字符串。

    Returns:
        root      : 虚拟根节点（level=0），包含完整的标题树
        all_chunks: 按出现顺序排列的所有 Chunk 列表
    """
    root = HeadingNode(level=0, title="__root__")
    all_chunks: list[Chunk] = []

    # heading_stack[0] 始终是 root；后续各层级按需入栈
    heading_stack: list[HeadingNode] = [root]

    # 将整个文档拆成「段落/标题行」序列
    lines = md_text.split("\n")
    buffer: list[str] = []  # 暂存当前标题下的普通文本行

    def flush_buffer(current_heading: HeadingNode):
        """将 buffer 中的内容按段落切块，挂到 current_heading 下。"""
        if not buffer:
            return
        text_block = "\n".join(buffer)
        for para in _split_paragraphs(text_block):
            chunk = Chunk(
                content=para,
                heading=current_heading,
                source_file=source_file,
            )
            current_heading.chunks.append(chunk)
            all_chunks.append(chunk)
        buffer.clear()

    def current_heading() -> HeadingNode:
        return heading_stack[-1]

    for line in lines:
        m = _HEADING_RE.match(line)
        if m:
            # 遇到标题行：先把已有缓冲切块
            flush_buffer(current_heading())

            level = len(m.group(1))
            title = m.group(2).strip()

            # 弹出栈中所有 level >= 当前级别的节点
            while len(heading_stack) > 1 and heading_stack[-1].level >= level:
                heading_stack.pop()

            parent = heading_stack[-1]
            node = HeadingNode(level=level, title=title, parent=parent)
            parent.children.append(node)
            heading_stack.append(node)
        else:
            buffer.append(line)

    # 处理文档末尾残余内容
    flush_buffer(current_heading())

    return root, all_chunks


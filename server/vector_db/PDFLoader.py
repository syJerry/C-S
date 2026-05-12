from concurrent.futures import ThreadPoolExecutor

import pymupdf
import pymupdf4llm
import re
from collections import Counter
import os

from logzero import logger
from tqdm import tqdm
import concurrent.futures


class PDFLoader:
    """
    自定义pdf加载器，主要处理pymupdf4llm标题级别识别错误的问题，使用统计字体大小来重新处理标题
    """

    def __init__(self, threads=None):
        self.thread_nums = os.cpu_count()
        if threads:
            self.thread_nums = threads

    @staticmethod
    def loader(pdf_path: str, progress=False) -> list[str]:
        loder = Loader(pdf_path, progress)
        md_text = loder.convert_pdf_to_md()
        return [md_text]

    @staticmethod
    def loder_from_dir(pdf_dir: str, max_worker: int) -> list[str]:
        pdf_files = []
        for root, dirs, files in os.walk(pdf_dir):
            for file in files:
                if file.endswith('.pdf'):
                    pdf_files.append(os.path.join(root, file))
        res = []
        if max_worker <= 0:
            for path in pdf_files:
                res += PDFLoader.loader(path)
        else:
            res = PDFLoader.load_pdfs_with_progress(pdf_files, max_worker)
        return res

    @staticmethod
    def load_pdfs_with_progress(pdf_files, max_worker):
        """带进度条的并行加载"""
        results = []
        total_files = len(pdf_files)

        with ThreadPoolExecutor(max_workers=max_worker) as executor:
            # 提交所有任务
            future_to_path = {executor.submit(PDFLoader.loader, pdf_path, False): pdf_path
                              for pdf_path in pdf_files}

            # 使用tqdm显示进度
            with tqdm(total=total_files, desc="加载PDF文件") as pbar:
                for future in concurrent.futures.as_completed(future_to_path):
                    pdf_path = future_to_path[future]
                    try:
                        result = future.result()
                        results.append(result)
                    except Exception as e:
                        logger.info(f"加载 {os.path.basename(pdf_path)} 时出错: {e}")
                    finally:
                        pbar.update(1)

        return results


class Loader:
    def __init__(self, pdf_path: str, progress=False):
        self.progress = progress
        self.doc = None
        self.pdf_path = pdf_path

    def build_font_size_heading_map(self) -> dict[float, int]:
        """
        分析 PDF 中所有文本的字号，推断哪些字号对应标题及其层级。
        :param
        :return: {字号: 标题级别(1/2/3...)}，正文字号作为最后级别标题字号。
        """
        self.doc = pymupdf.open(self.pdf_path)
        size_counter = Counter()

        for page in self.doc:
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        size = round(span["size"], 1)
                        text = span["text"].strip()
                        if text:  # 忽略空白文本
                            size_counter[size] += len(text)

        # 字符数最多的字号视为正文
        body_size = size_counter.most_common(1)[0][0]
        logger.info(f"正文字号推断: {body_size}")

        # 找出比正文大的字号，从大到小排列 → 对应 H1, H2, H3...
        heading_sizes = sorted(
            [s for s in size_counter if s >= body_size],
            reverse=True
        )
        logger.info(f"标题字号(从大到小): {heading_sizes}")
        return {size: level + 1 for level, size in enumerate(heading_sizes)}

    def build_text_size_index(self, size_map: dict) -> dict[str, int]:
        """
        遍历 PDF，记录所有属于标题字号的文本行及其对应的标题级别。
        :param size_map: dict{字号：标题级别}
        :return: {清理后的文本: 标题级别}
        """
        index = {}

        for page in self.doc:
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                for line in block.get("lines", []):
                    spans = line.get("spans", [])
                    if not spans:
                        continue

                    # 取该行最大字号作为代表
                    max_size = max(round(s["size"], 1) for s in spans)
                    if max_size not in size_map:
                        continue

                    # 合并该行所有 span 的文本
                    line_text = "".join(s["text"] for s in spans).strip()
                    line_text_clean = re.sub(r'\s+', ' ', line_text)

                    if line_text_clean:
                        index[line_text_clean] = size_map[max_size]
        return index

    def fix_heading_levels(self, md_text: str, text_size_index: dict) -> str:
        """
        对照 text_size_index，修正 MD 中每个标题行的 # 级别。
        匹配时忽略 markdown 粗体符号(**) 和首尾空格，使用模糊匹配。
        :param md_text: pymupdf4llm处理得到的.md数据
        :param text_size_index:
        :return:
        """
        lines = md_text.split('\n')
        result = []
        fixed_count = 0

        heading_re = re.compile(r'^(#{1,6})\s+(.*)')

        for line in lines:
            m = heading_re.match(line)
            if m:
                current_level = len(m.group(1))
                heading_text = m.group(2)

                # 清理 markdown 符号后用于匹配
                clean_text = re.sub(r'\*+', '', heading_text).strip()
                clean_text = re.sub(r'\s+', ' ', clean_text)

                # 精确匹配 → 模糊匹配（处理连字符/空格差异）
                matched_level = (
                        text_size_index.get(clean_text) or
                        self._fuzzy_match(clean_text, text_size_index)
                )

                if matched_level and matched_level != current_level:
                    line = '#' * matched_level + ' ' + heading_text
                    fixed_count += 1

            result.append(line)

        logger.info(f"共修正标题 {fixed_count} 处")
        return '\n'.join(result)

    @staticmethod
    def _fuzzy_match(text: str, index: dict, threshold: float = 0.85) -> int | None:
        """简单模糊匹配：处理 pymupdf4llm 和 pymupdf 提取文本的细微差异"""
        text_lower = text.lower()
        for key, level in index.items():
            key_lower = key.lower()
            # 包含关系匹配
            if text_lower in key_lower or key_lower in text_lower:
                ratio = len(min(text, key, key=len)) / len(max(text, key, key=len))
                if ratio >= threshold:
                    return level
        return None

    def convert_pdf_to_md(self):
        # 1. 分析字号，建立映射
        size_map = self.build_font_size_heading_map()
        if not size_map:
            logger.info("未检测到标题字号，跳过修正")
            return
        # 2. 建立文本→级别索引
        text_index = self.build_text_size_index(size_map)
        logger.info(f"索引标题数: {len(text_index)} 条")

        # 3. pymupdf4llm 转换
        md = pymupdf4llm.to_markdown(self.doc, header=False, footer=False, show_progress=self.progress)

        # 4. 修正标题层级
        fixed_md = self.fix_heading_levels(md, text_index)

        return fixed_md

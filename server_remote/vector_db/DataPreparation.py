from datetime import datetime

from vector_db.PDFLoader import PDFLoader
from vector_db.MarkdownParse import MarkdownParse


class DataPreparation:
    @staticmethod
    def loadPDF(pdf_path):
        md_texts = PDFLoader.loader(pdf_path,True)
        md_data = MarkdownParse.Parse2Markdown(md_texts)
        return md_data


if __name__ == "__main__":
    path = "../data/blog_clean.pdf"
    print("=" * 60)
    start = datetime.now()
    md_text = PDFLoader.loader(path, True)
    end = datetime.now()
    elapsed = end - start
    print(f"pdf处理耗时：{elapsed.total_seconds():.2f} 秒")
    print("=" * 60)
    print("=" * 60)
    start = datetime.now()
    md = MarkdownParse.Parse2Markdown(md_text)
    end = datetime.now()
    elapsed = end - start
    print(f"md处理耗时：{elapsed.total_seconds():.2f} 秒")
    print(f"获得块数：{md.chunk_count}")
    print(md.docs[-1].page_content)
    # with open("test.md", "w", encoding="utf-8") as f:
    #     f.write(md_text[0])

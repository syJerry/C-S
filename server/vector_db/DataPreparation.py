from datetime import datetime
from pathlib import Path
from vector_db.PDFLoader import PDFLoader
from vector_db.MarkdownParse import MarkdownParse


class DataPreparation:
    @staticmethod
    def loadPDF(pdf_path):
        md_texts = PDFLoader.loader(pdf_path,False)
        md_data = MarkdownParse.Parse2Markdown(md_texts)
        return md_data

    @staticmethod
    def loadData(directory):
        md_texts = []

        directory = Path(directory)

        for file_path in directory.rglob("*"):
            if not file_path.is_file():
                continue

            suffix = file_path.suffix.lower()

            if suffix == ".pdf":
                # PDFLoader.loader 返回 list[str]
                pdf_texts = PDFLoader.loader(str(file_path), False)
                md_texts.extend(pdf_texts)

            elif suffix == ".md":
                # Markdown 文件直接读入为 str
                with open(file_path, "r", encoding="utf-8") as f:
                    md_texts.append(f.read())

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

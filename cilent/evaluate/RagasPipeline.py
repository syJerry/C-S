import asyncio
import os
import json
import time
import pandas as pd
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness
from ragas.metrics._answer_relevance import answer_relevancy
from ragas.metrics import context_precision
from model_util.Model import llm, embedding


# =========================
# 1. 路径配置
# =========================

QUESTION_FILE = "./evaluate/questions.txt"

OUTPUT_DIR = "statistics/ragas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

RAW_JSONL_PATH = os.path.join(OUTPUT_DIR, "ragas_raw_data.jsonl")
DATASET_JSON_PATH = os.path.join(OUTPUT_DIR, "ragas_dataset.json")
DETAIL_CSV_PATH = os.path.join(OUTPUT_DIR, "ragas_detail_result.csv")
DETAIL_EXCEL_PATH = os.path.join(OUTPUT_DIR, "ragas_detail_result.xlsx")


# =========================
# 2. 工具函数
# =========================

def read_questions(path: str):
    with open(path, "r", encoding="utf-8") as f:
        questions = [line.strip() for line in f if line.strip()]
    return questions


def doc_to_text(doc):
    """
    兼容 LangChain Document / 普通字符串 / 字典
    """
    if isinstance(doc, str):
        return doc

    if hasattr(doc, "page_content"):
        return doc.page_content

    if isinstance(doc, dict):
        return doc.get("page_content", str(doc))

    return str(doc)


def load_finished_questions(jsonl_path: str):
    """
    读取已经完成的问题，用于断点续跑
    """
    finished = set()

    if not os.path.exists(jsonl_path):
        return finished

    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                finished.add(item["question"])

    return finished


def append_jsonl(path: str, item: dict):
    """
    每生成一条就立刻写入磁盘
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
        f.flush()


def load_jsonl(path: str):
    data = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))

    return data


# =========================
# 3. 生成 RAGAS 原始数据
# =========================

def build_ragas_raw_data(rag_system):
    """
    rag_system 需要提供：
    rag_system.generate(question: str) -> {
        "answer": str,
        "docs": List[Document]
    }
    """

    questions = read_questions(QUESTION_FILE)
    finished_questions = load_finished_questions(RAW_JSONL_PATH)

    print(f"总问题数: {len(questions)}")
    print(f"已完成数: {len(finished_questions)}")

    for idx, question in enumerate(questions, start=1):
        if question in finished_questions:
            print(f"[跳过] {idx}/{len(questions)} {question}")
            continue

        print(f"[生成] {idx}/{len(questions)} {question}")

        try:
            result = rag_system.generate(question)

            answer = result["answer"]
            docs = result["docs"]

            contexts = [doc_to_text(doc) for doc in docs]

            item = {
                "question": question,
                "answer": answer,
                "contexts": contexts,
                "doc_count": len(contexts),
                "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }

            append_jsonl(RAW_JSONL_PATH, item)

        except Exception as e:
            error_item = {
                "question": question,
                "answer": "",
                "contexts": [],
                "error": str(e),
                "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }

            append_jsonl(RAW_JSONL_PATH, error_item)
            print(f"[错误] {question}: {e}")


# =========================
# 4. 构建并保存 RAGAS Dataset
# =========================

def build_and_save_dataset():
    raw_data = load_jsonl(RAW_JSONL_PATH)

    valid_data = [
        item for item in raw_data
        if item.get("answer") and item.get("contexts")
    ]

    data = {
        "question": [item["question"] for item in valid_data],
        "answer": [item["answer"] for item in valid_data],
        "contexts": [item["contexts"] for item in valid_data],
    }

    dataset = Dataset.from_dict(data)

    with open(DATASET_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"有效样本数: {len(valid_data)}")
    print(f"Dataset 已保存到: {DATASET_JSON_PATH}")

    return dataset


# =========================
# 5. 构建中文 answer_relevancy
# =========================

def build_chinese_answer_relevancy():
    prompt = answer_relevancy.get_prompts()
    p = {"response_relevance_prompt": asyncio.run(prompt["response_relevance_prompt"].adapt("chinese", llm, True))}
    answer_relevancy.set_prompts(**p)


# =========================
# 6. 运行 RAGAS 评测并保存逐条结果
# =========================

def run_ragas_evaluation():
    dataset = build_and_save_dataset()

    build_chinese_answer_relevancy()

    result = evaluate(
        dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision
        ],
        llm=llm,
        embeddings=embedding
    )

    df = result.to_pandas()

    df.to_csv(DETAIL_CSV_PATH, index=False, encoding="utf-8-sig")
    df.to_excel(DETAIL_EXCEL_PATH, index=False)

    print("整体结果:")
    print(result)

    print(f"逐条结果 CSV 已保存到: {DETAIL_CSV_PATH}")
    print(f"逐条结果 Excel 已保存到: {DETAIL_EXCEL_PATH}")

    return df


# =========================
# 7. 总入口
# =========================

def run_pipeline(rag_system):
    build_ragas_raw_data(rag_system)
    df = run_ragas_evaluation()
    return df
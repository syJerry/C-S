"""
RAG 检索评测工具。

评测指标：
- 准确率
- 召回率
- 平均向量相似度
- 检索耗时
"""

import csv
import json
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Callable, List, Optional

from json_repair import repair_json
from langchain.schema import Document
from sentence_transformers import util

from model_util.Model import embedding, llm_message


@dataclass
class TestCase:
    query: str
    k: int
    description: str
    # 如果已知真实相关文档总数，可用作召回率分母。
    total_relevant: Optional[int] = None


@dataclass
class TestResult:
    query: str
    description: str
    k: int
    retrieval_time_ms: float
    retrieved_count: int
    relevant_count: int
    total_relevant: int
    precision: float
    recall: float
    avg_similarity: float
    documents: List[dict] = field(default_factory=list)
    llm_judgments: List[bool] = field(default_factory=list)


_JUDGE_SYSTEM = """你是一名严格的文档相关性评估专家。
给定一个用户查询和一篇文档，请判断该文档是否与查询相关。

相关的标准：文档内容能够直接或间接回答、支持或补充用户查询涉及的主题。
不相关的标准：文档内容与查询主题无关，或只有表面词汇重叠但语义无关。

{human_message}

请严格按照以下 JSON 格式返回，不要输出任何其他内容：
{
  "relevant": true
}
"""


def judge_relevance_with_llm(query: str, documents: List[Document]) -> List[bool]:
    """逐条判断文档相关性，并汇总布尔结果。"""
    judgments: List[bool] = []

    for index, doc in enumerate(documents, start=1):
        content = doc.page_content
        user_message = f"""查询：{query}

[文档 {index}]
{content}
"""
        response = llm_message(_JUDGE_SYSTEM, user_message, "relevance_judge")
        raw = repair_json(response)
        parsed = json.loads(raw)

        relevant = parsed.get("relevant")
        if relevant is None:
            # 兼容旧版批量输出格式。
            legacy_judgments = parsed.get("judgments", [])
            relevant = legacy_judgments[0] if legacy_judgments else False

        judgments.append(bool(relevant))

    return judgments


def compute_similarity(query: str, docs: list[str]):
    texts = [query] + docs
    embeddings = embedding.encode(texts, convert_to_tensor=True)

    query_embedding = embeddings[0]
    doc_embeddings = embeddings[1:]
    similarities = util.cos_sim(query_embedding, doc_embeddings)[0]

    results = []
    for doc, score in zip(docs, similarities):
        results.append({
            "document": doc,
            "similarity": float(score),
        })

    return {
        "query": query,
        "results": results,
    }


def extract_similarity(query: str, docs: list[Document]) -> Optional[list[float]]:
    docs_str = [doc.page_content for doc in docs]
    response = compute_similarity(query, docs_str)

    similarities: list[float] = []
    for item in response["results"]:
        similarities.append(item["similarity"])
    return similarities


RetrieveFn = Callable[[str, int, str], List[Document]]


def run_single_test(
    retrieve: RetrieveFn,
    test_case: TestCase,
    verbose: bool = True,
) -> TestResult:
    query = test_case.query
    k = test_case.k
    desc = test_case.description

    if verbose:
        print(f"\n{'=' * 60}")
        print(f"  查询     : {query}")
        print(f"  描述     : {desc}")
        print(f"  Top-K    : {k}")

    start = time.perf_counter()
    docs: List[Document] = retrieve(query, k, desc)
    elapsed_ms = (time.perf_counter() - start) * 1000

    retrieved_count = len(docs)
    if verbose:
        print(f"  检索耗时 : {elapsed_ms:.1f} ms  |  文档数: {retrieved_count}")

    sims = extract_similarity(query, docs)
    valid_sims = [score for score in sims if score is not None]
    avg_similarity = sum(valid_sims) / len(valid_sims) if valid_sims else 0.0
    if verbose:
        print(f"  相似度   : {[round(score, 4) if score is not None else 'N/A' for score in sims]}")
        print(f"  平均相似度: {avg_similarity:.4f}")

    if verbose:
        print("  正在调用 LLM 逐条判断文档相关性...")
    judgments = judge_relevance_with_llm(query, docs)
    relevant_count = sum(judgments)

    precision = relevant_count / retrieved_count if retrieved_count > 0 else 0.0
    total_relevant = test_case.total_relevant if test_case.total_relevant is not None else relevant_count
    recall = relevant_count / total_relevant if total_relevant > 0 else 0.0

    if verbose:
        print(f"  LLM 判断  : {judgments}")
        print(f"  准确率    : {precision:.4f}  |  召回率: {recall:.4f}")

    doc_summaries = []
    for index, (doc, sim, is_rel) in enumerate(zip(docs, sims, judgments), start=1):
        doc_summaries.append({
            "index": index,
            "relevant": is_rel,
            "similarity": round(sim, 4) if sim is not None else None,
            "content_preview": doc.page_content[:200],
            "metadata": doc.metadata,
        })

    return TestResult(
        query=query,
        description=desc,
        k=k,
        retrieval_time_ms=round(elapsed_ms, 2),
        retrieved_count=retrieved_count,
        relevant_count=relevant_count,
        total_relevant=total_relevant,
        precision=round(precision, 4),
        recall=round(recall, 4),
        avg_similarity=round(avg_similarity, 4),
        documents=doc_summaries,
        llm_judgments=judgments,
    )


def run_tests(
    retrieve: RetrieveFn,
    test_cases: List[TestCase],
    output_json: str = "rag_test_results.json",
    output_csv: str = "rag_test_summary.csv",
    verbose: bool = True,
) -> List[TestResult]:
    print(f"\n{'#' * 60}")
    print(f"  RAG 检索评测开始（共 {len(test_cases)} 个用例）")
    print(f"{'#' * 60}")

    results: List[TestResult] = []
    for test_case in test_cases:
        result = run_single_test(retrieve, test_case, verbose=verbose)
        results.append(result)
        time.sleep(1.0)

    avg_precision = sum(result.precision for result in results) / len(results)
    avg_recall = sum(result.recall for result in results) / len(results)
    avg_sim_all = sum(result.avg_similarity for result in results) / len(results)
    avg_time = sum(result.retrieval_time_ms for result in results) / len(results)

    print(f"\n{'#' * 60}")
    print("  汇总结果")
    print(f"  平均准确率   : {avg_precision:.4f}")
    print(f"  平均召回率   : {avg_recall:.4f}")
    print(f"  平均相似度   : {avg_sim_all:.4f}")
    print(f"  平均检索耗时 : {avg_time:.1f} ms")
    print(f"{'#' * 60}\n")

    timestamp = datetime.now().isoformat()
    json_payload = {
        "test_time": timestamp,
        "total_cases": len(results),
        "summary": {
            "avg_precision": round(avg_precision, 4),
            "avg_recall": round(avg_recall, 4),
            "avg_similarity": round(avg_sim_all, 4),
            "avg_retrieval_time_ms": round(avg_time, 2),
        },
        "results": [asdict(result) for result in results],
    }
    with open(output_json, "w", encoding="utf-8") as file:
        json.dump(json_payload, file, ensure_ascii=False, indent=2)
    print(f"  详细结果已保存到: {output_json}")

    csv_fields = [
        "query",
        "description",
        "k",
        "retrieval_time_ms",
        "retrieved_count",
        "relevant_count",
        "total_relevant",
        "precision",
        "recall",
        "avg_similarity",
    ]
    with open(output_csv, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=csv_fields)
        writer.writeheader()
        for result in results:
            row = asdict(result)
            writer.writerow({field: row[field] for field in csv_fields})
    print(f"  摘要 CSV 已保存到: {output_csv}\n")

    return results


if __name__ == "__main__":
    def mock_retrieve(query: str, k: int, description: str) -> List[Document]:
        return [
            Document(
                page_content=f"这是一条与“{query}”相关的模拟文档内容，示例 {index + 1}。",
                metadata={"source": f"doc_{index + 1}.txt", "score": 0.95 - index * 0.05},
            )
            for index in range(k)
        ]

    test_cases = [
        TestCase(
            query="什么是 RAG？",
            k=5,
            description="RAG 基础概念查询",
            total_relevant=8,
        ),
        TestCase(
            query="向量数据库的对比",
            k=3,
            description="向量数据库比较",
        ),
        TestCase(
            query="如何提升 embedding 检索效果？",
            k=5,
            description="embedding 优化策略",
            total_relevant=6,
        ),
    ]

    run_tests(
        retrieve=mock_retrieve,
        test_cases=test_cases,
        output_json="rag_test_results.json",
        output_csv="rag_test_summary.csv",
    )

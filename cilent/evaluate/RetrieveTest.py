"""
RAG 检索模块测试工具
===================
测试指标：准确率、召回率、向量相似度平均值、检索时间
依赖：langchain, anthropic
"""

import time
import json
import csv
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import Callable, List, Optional

import numpy as np
import requests
from json_repair import repair_json
from langchain_core.documents import Document
# from langchain.schema import Document
from langchain_core.messages import SystemMessage, HumanMessage

from model_util import Prompt
from model_util.Model import llm, embedding


# ─────────────────────────────────────────────
# 数据结构
# ─────────────────────────────────────────────

@dataclass
class TestCase:
    query: str
    k: int
    description: str
    # 如果已知相关文档数（Ground Truth 总数），可用于计算召回率分母
    # 若不填则以 LLM 判断到的相关数为分母（即 precision == recall）
    total_relevant: Optional[int] = None


@dataclass
class TestResult:
    query: str
    description: str
    k: int
    retrieval_time_ms: float
    retrieved_count: int
    relevant_count: int           # LLM 判断相关数
    total_relevant: int           # 真实相关总数（用于召回率分母）
    precision: float
    recall: float
    avg_similarity: float
    documents: List[dict] = field(default_factory=list)  # 检索到的文档摘要
    llm_judgments: List[bool] = field(default_factory=list)


# ─────────────────────────────────────────────
# LLM 相关性判断
# ─────────────────────────────────────────────
_JUDGE_SYSTEM = """你是一个严格的文档相关性评估专家。
给定一个用户查询和一批文档，你需要判断每个文档是否与查询相关。

相关的标准：文档内容能直接或间接回答、支持或补充用户查询所涉及的主题。
不相关的标准：文档内容与查询主题无关，或仅有表面词汇重叠但语义无关。

请严格按照以下 JSON 格式返回，不要输出任何其他内容：
{
  "judgments": [true, false, ...]   // 布尔数组，顺序与输入文档一致
}
"""


def judge_relevance_with_llm(query: str, documents: List[Document]) -> List[bool]:
    """调用 Claude 判断每个文档是否与 query 相关，返回布尔列表。"""
    doc_texts = []
    for i, doc in enumerate(documents):
        content = doc.page_content[:800]  # 截断避免超 token
        doc_texts.append(f"[文档 {i+1}]\n{content}")

    user_message = f"""查询：{query}

共有{len(documents)}个文档,以[文档 i]为起始位置,文档列表：
{chr(10).join(doc_texts)}
请判断以上每个文档是否与查询相关，返回 JSON。"""

    # print(docs_str)
    # url = "http://127.0.0.1:43421/judge"
    # data = {
    #     "query": user_message,
    # }
    # time.sleep(5)
    # response = requests.post(url, json=data)
    # raw = response.json()["response"]
    messages = [
        SystemMessage(content=_JUDGE_SYSTEM),
        HumanMessage(content=user_message),
    ]
    response = llm(messages)
    raw = response.content
    # 清理可能的 markdown 代码块
    # raw = raw.replace("```json", "").replace("```", "").strip()
    raw = repair_json(raw)
    parsed = json.loads(raw)
    judgments = parsed["judgments"]

    # 保证长度与文档数一致
    if len(judgments) < len(documents):
        judgments += [False] * (len(documents) - len(judgments))
    return judgments[:len(documents)]


# ─────────────────────────────────────────────
# 相似度提取工具
# ─────────────────────────────────────────────
def extract_similarity(query:str,docs: list[Document]) -> Optional[list[float]]:
    """从 Document.metadata 中尝试提取相似度分数。
    常见字段：score, similarity, relevance_score, distance（转换）。
    """
    docs_str = [d.page_content for d in docs]
    # print(docs_str)
    time.sleep(5)
    url = "http://127.0.0.1:43421/similarity"
    data = {
        "query": query,
        "documents": docs_str
    }
    response = requests.post(url, json=data)
    # print(response.json())
    res = []
    for d in response.json()["results"]:
        res.append(d["similarity"])
    return res

# ─────────────────────────────────────────────
# 核心测试函数
# ─────────────────────────────────────────────

RetrieveFn = Callable[[str, int, str], List[Document]]


def run_single_test(
    retrieve: RetrieveFn,
    test_case: TestCase,
    verbose: bool = True,
) -> TestResult:
    """执行单条测试用例，返回 TestResult。"""
    query = test_case.query
    k = test_case.k
    desc = test_case.description

    if verbose:
        print(f"\n{'─' * 60}")
        print(f"  查询    : {query}")
        print(f"  描述    : {desc}")
        print(f"  Top-K   : {k}")

    # 1. 检索 & 计时
    start = time.perf_counter()
    docs: List[Document] = retrieve(query, k, desc)
    elapsed_ms = (time.perf_counter() - start) * 1000

    retrieved_count = len(docs)
    if verbose:
        print(f"  检索时间: {elapsed_ms:.1f} ms  |  返回文档数: {retrieved_count}")

    # 2. 向量相似度
    sims = extract_similarity(query,docs)
    valid_sims = [s for s in sims if s is not None]
    weights = [1 / (i + 1) for i in range(len(valid_sims))]
    avg_similarity = sum(s * w for s, w in zip(valid_sims, weights)) / sum(weights)
    if verbose:
        print(f"  相似度  : {[round(s, 4) if s is not None else 'N/A' for s in sims]}")
        print(f"  加权相似度: {avg_similarity:.4f}")

    # 3. LLM 相关性判断
    if verbose:
        print("  正在调用 LLM 判断相关性...")
    judgments = judge_relevance_with_llm(query, docs)
    relevant_count = sum(judgments)

    # 4. 计算准确率 & 召回率
    precision = relevant_count / retrieved_count if retrieved_count > 0 else 0.0
    total_relevant = test_case.total_relevant if test_case.total_relevant is not None else relevant_count
    recall = relevant_count / total_relevant if total_relevant > 0 else 0.0

    if verbose:
        print(f"  LLM 判断: {judgments}")
        print(f"  准确率  : {precision:.4f}  |  召回率: {recall:.4f}")

    # 5. 整理文档摘要
    doc_summaries = []
    for i, (doc, sim, is_rel) in enumerate(zip(docs, sims, judgments)):
        doc_summaries.append({
            "index": i + 1,
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


# ─────────────────────────────────────────────
# 批量测试 & 结果保存
# ─────────────────────────────────────────────

def run_tests(
    retrieve: RetrieveFn,
    test_cases: List[TestCase],
    output_json: str = "rag_test_results.json",
    output_csv: str = "rag_test_summary.csv",
    verbose: bool = True,
) -> List[TestResult]:
    """
    批量运行测试用例，结果同时保存为 JSON（详细）和 CSV（摘要）。

    Parameters
    ----------
    retrieve    : 检索函数，签名 retrieve(query, k, description) -> List[Document]
    test_cases  : 测试用例列表
    output_json : 详细结果保存路径
    output_csv  : 摘要 CSV 保存路径
    verbose     : 是否打印过程日志
    """
    print(f"\n{'═' * 60}")
    print(f"  RAG 检索模块测试开始  ({len(test_cases)} 个用例)")
    print(f"{'═' * 60}")

    results: List[TestResult] = []
    for tc in test_cases:
        result = run_single_test(retrieve, tc, verbose=verbose)
        results.append(result)
        time.sleep(1.0)

    # ── 汇总统计 ──────────────────────────────
    avg_precision = sum(r.precision for r in results) / len(results)
    avg_recall = sum(r.recall for r in results) / len(results)
    avg_sim_all = sum(r.avg_similarity for r in results) / len(results)
    avg_time = sum(r.retrieval_time_ms for r in results) / len(results)

    print(f"\n{'═' * 60}")
    print("  汇总结果")
    print(f"  平均准确率    : {avg_precision:.4f}")
    print(f"  平均召回率    : {avg_recall:.4f}")
    print(f"  平均向量相似度: {avg_sim_all:.4f}")
    print(f"  平均检索时间  : {avg_time:.1f} ms")
    print(f"{'═' * 60}\n")

    # ── 保存 JSON ─────────────────────────────
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
        "results": [asdict(r) for r in results],
    }
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(json_payload, f, ensure_ascii=False, indent=2)
    print(f"  详细结果已保存 → {output_json}")

    # ── 保存 CSV ──────────────────────────────
    csv_fields = [
        "query", "description", "k", "retrieval_time_ms",
        "retrieved_count", "relevant_count", "total_relevant",
        "precision", "recall", "avg_similarity",
    ]
    with open(output_csv, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for r in results:
            row = asdict(r)
            writer.writerow({k: row[k] for k in csv_fields})
    print(f"  摘要 CSV 已保存 → {output_csv}\n")

    return results



if __name__ == "__main__":
    # ── 请替换为你真实的 retrieve 函数 ──────────
    # from your_module import retrieve
    #
    # 函数签名示例：
    #   def retrieve(query: str, k: int, description: str) -> List[Document]:
    #       ...

    # ── 示例：用 Mock 数据演示 ─────────────────
    def mock_retrieve(query: str, k: int, description: str) -> List[Document]:
        """演示用的 Mock 检索函数，请替换为真实实现。"""
        return [
            Document(
                page_content=f"这是与'{query}'相关的文档内容示例 {i+1}。",
                metadata={"source": f"doc_{i+1}.txt", "score": 0.95 - i * 0.05},
            )
            for i in range(k)
        ]

    test_cases = [
        TestCase(
            query="什么是 RAG（检索增强生成）？",
            k=5,
            description="RAG 基础概念查询",
            total_relevant=8,   # 假设语料库中共有 8 篇相关文档
        ),
        TestCase(
            query="向量数据库的选型对比",
            k=3,
            description="向量数据库比较",
            # 不填 total_relevant 时，召回率分母 = LLM 判断相关数
        ),
        TestCase(
            query="如何优化 embedding 模型的检索效果？",
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
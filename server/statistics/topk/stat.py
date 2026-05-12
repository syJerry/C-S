import json
import csv
import argparse


def weighted_average_similarities(documents):
    """
    对 documents 中的 similarity 做加权平均。
    排名越靠前，权重越高。

    例如共有 n 条：
    第 1 条权重 n
    第 2 条权重 n-1
    ...
    第 n 条权重 1
    """
    n = len(documents)

    if n == 0:
        return None

    total_weight = 0
    weighted_sum = 0.0

    for rank, doc in enumerate(documents, start=1):
        weight = n - rank + 1
        similarity = doc.get("similarity", 0)

        weighted_sum += similarity * weight
        total_weight += weight

    return weighted_sum / total_weight


def calculate_stats(data, k):
    rows = []

    results = data.get("results", [])

    for result_index, result_item in enumerate(results, start=1):
        documents = result_item.get("documents", [])

        top_k_docs = documents[:k]
        actual_k = len(top_k_docs)

        if actual_k == 0:
            relevant_accuracy = None
            weighted_similarity = None
            relevant_count = 0
        else:
            relevant_count = sum(
                1 for doc in top_k_docs
                if doc.get("relevant") is True
            )

            relevant_accuracy = relevant_count / actual_k
            weighted_similarity = weighted_average_similarities(top_k_docs)

        rows.append({
            "result_index": result_index,
            "k": k,
            "actual_k": actual_k,
            "relevant_count": relevant_count,
            "relevant_accuracy": relevant_accuracy,
            "weighted_similarity": weighted_similarity
        })

    return rows


def save_to_csv(rows, output_path):
    fieldnames = [
        "result_index",
        "k",
        "actual_k",
        "relevant_count",
        "relevant_accuracy",
        "weighted_similarity"
    ]

    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    input = "./topk_results_25.json"
    with open(input, "r", encoding="utf-8") as f:
        data = json.load(f)
        for k in [5,10,15,20,25]:
            rows = calculate_stats(data, k)

            save_to_csv(rows, f"output_{k}.csv")

            print(f"统计完成，结果已保存到: ")


if __name__ == "__main__":
    main()
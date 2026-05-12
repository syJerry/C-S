from typing import List, Tuple, Dict, Any

import requests
from langchain.schema import Document, SystemMessage, HumanMessage
from logzero import logger

# from model_util import Prompt


class Chat:
    def __init__(self, chat_id, top_k=10
                 ):
        self.chat_id = chat_id
        self.top_k = top_k
        self.history: List[Dict[str, str]] = []
        self.summary: str = ""

    def retrieve(self, query: str) -> List[Document]:
        url = "http://localhost:43421/retrieve"

        payload = {
            "query": query,
            "top_k": self.top_k
        }
        try:
            resp = requests.post(url, json=payload)
            resp.raise_for_status()
            data = resp.json()
            documents = [
                Document(
                    page_content=doc["page_content"],
                    metadata=doc.get("metadata", {})
                )
                for doc in data["documents"]
            ]
            return documents

        except requests.exceptions.Timeout:
            return []

        except requests.exceptions.ConnectionError:
            return []

        except requests.exceptions.HTTPError as e:
            return []

        except Exception as e:
            return []

    def build_context(self, docs: List[Document]) -> Tuple[str, List[str]]:
        context = ""
        list_context = []
        for idx, doc in enumerate(docs):
            context += f"[{idx}] {doc.page_content}\n"
            list_context.append(doc.page_content)
        return context, list_context

    def build_history_text(self, max_turns: int = 6) -> str:
        """
        将结构化历史转为 LLM 可读的文本
        只取最近 max_turns 轮
        """
        if len(self.history) == 0:
            return ""

        recent_history = self.history[-max_turns:]

        history_text = ""
        for turn in recent_history:
            history_text += f"用户：{turn['user']}\n"
            history_text += f"助手：{turn['assistant']}\n"
        return history_text

    def build_messages(self, question: str, context: str):
        user_prompt = (
            f"【参考资料】\n{context}\n\n"
            f"【问题】\n{question}"
        )

        history_prompt = self.build_history_text(self.top_k)
        # messages = [
        #     SystemMessage(content=Prompt.SYSTEM_PROMPT),
        #     HumanMessage(content=history_prompt + user_prompt),
        # ]
        return history_prompt + user_prompt

    def build_summary(self, question: str) -> str:
        user_prompt = (
            f"【用户问题】\n{question}"
        )
        payload = {
            "message": user_prompt
        }
        try:
            url = "http://localhost:43421/summary"
            resp = requests.post(url, json=payload)
            return resp.json()["response"]
        except:
            return ""

    def generate(self, question: str) -> Dict[str, Any]:
        if self.summary == "":
            self.summary = self.build_summary(question)
        docs = self.retrieve(question)
        logger.info(f"查询到{len(docs)}条内容。")
        context = self.build_context(docs)
        messages = self.build_messages(question, context[0])
        payload = {
            "message": messages
        }
        try:
            url = "http://localhost:43421/chat"
            resp = requests.post(url, json=payload)

            self.history.append({
                "user": question,
                "assistant": resp.json()["response"],
                "basis": context
            })
            return {
                "answer": resp.json()["response"],
                "docs": docs,
                "basis": context
            }
        except requests.exceptions.Timeout:
            return {
                "answer": "请求超时，请稍后重试",
                "docs": docs,
                "basis": context
            }

        except requests.exceptions.ConnectionError:
            return {
                "answer": "无法连接服务器，请检查网络",
                "docs": docs,
                "basis": context
            }

        except requests.exceptions.HTTPError as e:
            return {
                "answer": "服务异常",
                "docs": docs,
                "basis": context
            }
        except Exception as e:
            return {
                "answer": "未知错误",
                "docs": docs,
                "basis": context
            }
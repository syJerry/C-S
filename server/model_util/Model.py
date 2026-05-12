import os

from langchain_core.messages import HumanMessage
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from sentence_transformers import CrossEncoder
from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer
from config.load import json_config

from model.ChatGLM3.langchain_demo.ChatGLM3 import ChatGLM3
# llm = ChatOpenAI(
#     model_name=json_config['llm'].get('model'),
#     temperature=json_config['llm'].get('temperature'),
#     openai_api_key=json_config['llm'].get('api_key'),
#     openai_api_base=json_config['llm'].get('base_url')
# )
MODEL_PATH = os.environ.get('MODEL_PATH', '/store2/lzx25-tjr/server/model/ChatGLM3/Chatglm3-6B')
llm = ChatGLM3()
llm.load_model(MODEL_PATH)



class BGEEmbeddings(Embeddings):
    def __init__(self, model_path="./model/bge-large-zh", device="cuda:0"):
        self.model = SentenceTransformer(model_path, device=device)

    def embed_documents(self, texts):
        texts = ["为这个句子生成表示以用于检索：" + t for t in texts]
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )
        return embeddings.tolist()

    def embed_query(self, text):
        text = "为这个句子生成表示以用于检索：" + text
        embedding = self.model.encode(
            [text],
            normalize_embeddings=True
        )[0]
        return embedding.tolist()
    
    def encode(self, texts, convert_to_tensor=True):
        texts = ["为这个句子生成表示以用于检索：" + t for t in texts]
        embeddings = self.model.encode(
            texts,
            convert_to_tensor=convert_to_tensor
        )
        return embeddings

embedding = BGEEmbeddings(model_path="./model/bge-large-zh", device="cuda:0")

reranker_model = "./model/bge-reranker-v2-m3"  # 支持中文
reranker = CrossEncoder(
    reranker_model,
    device='cuda:0',
    max_length=512,
)

def llm_message(system_message,human_message,schema_type):
    allowed_schema_types = ["query_rewrite", "cited_answer", "relevance_judge", "chat","summary"]
    if schema_type not in allowed_schema_types:
        raise ValueError(f"Invalid schema_type. Must be one of {allowed_schema_types}")

    if schema_type == "chat" or schema_type == "summary":
        return llm(system_message.format(human_message = human_message), schema_type=None)
    # print("x"*60)
    # print(human_message)
    # print("x"*60)
    return llm(system_message.format(human_message = human_message),schema_type=schema_type)

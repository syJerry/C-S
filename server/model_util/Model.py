import os

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from sentence_transformers import CrossEncoder

from config.load import json_config

os.environ["OPENAI_API_KEY"] = json_config['llm'].get("api_key")

llm = ChatOpenAI(
    model_name=json_config['llm'].get('model'),
    temperature=json_config['llm'].get('temperature'),
    openai_api_key=json_config['llm'].get('api_key'),
    openai_api_base=json_config['llm'].get('base_url')
)

embedding = OpenAIEmbeddings(
    model=json_config['llm'].get('embedding'),
    openai_api_key=json_config['llm'].get('api_key'),
    openai_api_base=json_config['llm'].get('base_url')
)

reranker_model = "./model/bge-reranker-v2-m3"  # 支持中文
reranker = CrossEncoder(
    reranker_model,
    device='cpu',
    max_length=512,
)

def llm_message(system_message,human_message):
    return llm(system_message+"/n/n"+human_message)

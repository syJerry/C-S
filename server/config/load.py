import json
from pathlib import Path

from langchain_openai import OpenAIEmbeddings


def load_config(config_path: str) -> dict:
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_path}")
    with open(config_file, "r", encoding="utf-8") as f:
        return json.load(f)


def init_embedding(config: dict):
    emb_cfg = config.get("embedding")
    if emb_cfg is None:
        raise ValueError("配置中缺少 embedding 部分")

    provider = emb_cfg.get("provider")

    if provider == "openai":
        return OpenAIEmbeddings(
            model=emb_cfg.get("model"),
            openai_api_key=emb_cfg.get("api_key"),
            openai_api_base=emb_cfg.get("base_url"),
        )
    else:
        raise NotImplementedError(f"不支持的 embedding provider: {provider}")


json_config = load_config("./user.json")

from typing import Literal
import json

import torch
import xgrammar as xgr
from langchain.llms.base import LLM
from transformers import AutoConfig, AutoModel, AutoTokenizer


SCHEMAS = {
    "query_rewrite": {
        "type": "object",
        "properties": {
            "查询1": {"type": "string"},
            "查询2": {"type": "string"},
            "查询3": {"type": "string"},
            "查询4": {"type": "string"},
            "假设文档1": {"type": "string"},
            "假设文档2": {"type": "string"},
            "假设文档3": {"type": "string"},
            "假设文档4": {"type": "string"},
        },
        "required": [
            "查询1",
            "查询2",
            "查询3",
            "查询4",
            "假设文档1",
            "假设文档2",
            "假设文档3",
            "假设文档4",
        ],
        "additionalProperties": False,
    },
    "cited_answer": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "paragraph": {"type": "string"},
                "citations": {
                    "type": "array",
                    "items": {"type": "integer"},
                },
            },
            "required": ["paragraph", "citations"],
            "additionalProperties": False,
        },
    },
    "relevance_judge": {
        "type": "object",
        "properties": {
            "relevant": {"type": "boolean"},
        },
        "required": ["relevant"],
        "additionalProperties": False,
    },
}


SchemaType = Literal["query_rewrite", "cited_answer", "relevance_judge"]


class ChatGLM3(LLM):
    max_token: int = 8192
    do_sample: bool = False
    temperature: float = 0.2
    top_p: float = 0.8
    tokenizer: object = None
    model: object = None
    has_search: bool = False
    xgr_compiler: object = None

    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "ChatGLM3"

    def load_model(self, model_name_or_path: str = None):
        model_config = AutoConfig.from_pretrained(
            model_name_or_path,
            trust_remote_code=True,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path,
            trust_remote_code=True,
        )
        self.model = AutoModel.from_pretrained(
            model_name_or_path,
            config=model_config,
            trust_remote_code=True,
            device_map="auto",
        ).eval()

        tokenizer_info = xgr.TokenizerInfo.from_huggingface(
            self.tokenizer,
            vocab_size=model_config.vocab_size,
        )
        self.xgr_compiler = xgr.GrammarCompiler(tokenizer_info)

    def _call(self, prompt, stop=None, schema_type: SchemaType | None = "query_rewrite"):
        if schema_type == "query_rewrite":
            print(f"call chatglm3!{prompt}")
        if schema_type is None:
            response, _ = self.model.chat(self.tokenizer, prompt, history=[])
            return response

        schema = SCHEMAS[schema_type]
        compiled_grammar = self.xgr_compiler.compile_json_schema(
            json.dumps(schema, ensure_ascii=False)
        )
        logits_processor = xgr.contrib.hf.LogitsProcessor(compiled_grammar)

        inputs = self.tokenizer(prompt, return_tensors="pt")
        input_ids = inputs["input_ids"].to(self.model.device)

        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids,
                max_new_tokens=self.max_token,
                do_sample=self.do_sample,
                temperature=self.temperature if self.do_sample else 1.0,
                top_p=self.top_p if self.do_sample else 1.0,
                logits_processor=[logits_processor],
            )

        new_ids = output_ids[0][input_ids.shape[1]:]
        return self.tokenizer.decode(new_ids, skip_special_tokens=True)

    def call_query_rewrite(self, prompt: str) -> dict:
        raw = self._call(prompt, schema_type="query_rewrite")
        return json.loads(raw)

    def call_cited_answer(self, prompt: str) -> list:
        raw = self._call(prompt, schema_type="cited_answer")
        return json.loads(raw)

    def call_relevance_judge(self, prompt: str) -> dict:
        raw = self._call(prompt, schema_type="relevance_judge")
        return json.loads(raw)

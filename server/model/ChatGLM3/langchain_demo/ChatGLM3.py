from typing import Optional, Literal
import json

import xgrammar as xgr
import torch
from transformers.generation.utils import LogitsProcessorList
from transformers import AutoConfig, AutoTokenizer, AutoModel
from langchain.llms.base import LLM


# ── 所有 Schema 集中定义 ──────────────────────────────────────────
SCHEMAS = {
    # 查询改写 + 假设文档（HyDE / RAG-Fusion 风格）
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
        "required": ["查询1","查询2","查询3","查询4",
                     "假设文档1","假设文档2","假设文档3","假设文档4"],
        "additionalProperties": False,
    },

    # 带引用的分段回答
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

    # # 相关性判断（布尔数组）
    # "relevance_judge": {
    #     "type": "object",
    #     "properties": {
    #         "judgments": {
    #             "type": "array",
    #             "items": {"type": "boolean"},
    #         }
    #     },
    #     "required": ["judgments"],
    #     "additionalProperties": False,
    # },
        "relevance_judge": {
        "type": "object",
        "properties": {
            "relevant": {"type": "boolean"},
        },
        "required": ["relevant"],
        "additionalProperties": False,
    },
}

# Schema 类型的字面量，方便类型提示
SchemaType = Literal["query_rewrite", "cited_answer", "relevance_judge"]


class ChatGLM3(LLM):
    max_token: int = 8192
    do_sample: bool = True
    temperature: float = 0.3
    top_p: float = 0.7
    tokenizer: object = None
    model: object = None
    has_search: bool = False

    # XGrammar 编译器（懒加载，load_model 后初始化）
    xgr_compiler: object = None

    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "ChatGLM3"

    def load_model(self, model_name_or_path: str = None):
        device = torch.device("cuda:5")
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
            device_map="auto"
        ).eval()
        # print("x"*60)
        # print(self.model.device)
        # print("x"*60)

       
        tokenizer_info = xgr.TokenizerInfo.from_huggingface(
            self.tokenizer,
            vocab_size=model_config.vocab_size,  
        )
        self.xgr_compiler = xgr.GrammarCompiler(tokenizer_info)


    def _call(self, prompt, stop=None, schema_type="query_rewrite"):
        # if schema_type=="relevance_judge" :
        #     print(f"call chatglm3!{prompt}")
        if schema_type is None:
            print("没有格式约束！")
            response, _ = self.model.chat(self.tokenizer, prompt, history=[])
            return response

        schema = SCHEMAS[schema_type]
        compiled_grammar = self.xgr_compiler.compile_json_schema(
            json.dumps(schema, ensure_ascii=False)
        )
        processors = LogitsProcessorList()
        logits_processor = xgr.contrib.hf.LogitsProcessor(compiled_grammar)
        processors.append(logits_processor)
        # # inputs = self.tokenizer(prompt, return_tensors="pt",truncation=True, max_length=self.max_token//2)
        # inputs = self.tokenizer.build_chat_input(prompt, history=[], role="user")
        # input_ids = inputs["input_ids"].to(self.model.device)
        # eos_token_id = [self.tokenizer.eos_token_id, self.tokenizer.get_command("<|user|>"),
        #         self.tokenizer.get_command("<|observation|>")]
        # with torch.no_grad():
        #     output_ids = self.model.generate(
        #         input_ids,
        #         max_new_tokens=self.max_token//2,
        #         repetition_penalty=1.15,
        #         do_sample=self.do_sample,
        #         temperature=self.temperature,
        #         top_p=self.top_p,
        #         eos_token_id=eos_token_id,
        #         logits_processor=[logits_processor],
        #     )
        # new_ids = output_ids[0][input_ids.shape[1]:]
        # response = self.tokenizer.decode(new_ids, skip_special_tokens=True)
        response, _ = self.model.chat(self.tokenizer, prompt, history=[],logits_processor=processors)
        return response

    # ── 便捷包装方法（可选） ──────────────────────────────────────
    def call_query_rewrite(self, prompt: str) -> dict:
        raw = self._call(prompt, schema_type="query_rewrite")
        return json.loads(raw)

    def call_cited_answer(self, prompt: str) -> list:
        raw = self._call(prompt, schema_type="cited_answer")
        return json.loads(raw)

    def call_relevance_judge(self, prompt: str) -> dict:
        raw = self._call(prompt, schema_type="relevance_judge")
        return json.loads(raw)


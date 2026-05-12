# from evaluate.Exps import Exp4k, Exp4ablation
# exp4abl = Exp4ablation()
# exp4abl.run_exp()
from model_util import Prompt
from model_util.Model import llm_message
m  = """将下面提供的文档保持段落内容不变提取文档中的引用序号信息,下面是需要修改的文档内容，注意所有paragraph的value中应该是文档的所有内容：


输出格式是：
[
  {{
    "paragraph": "",
    "citations": []
  }},
  {{
    "paragraph": "",
    "citations": []
  }}
]

"""

print(llm_message(Prompt.PROCESS_PROMPT, "什么是SQL注入？[1]根据提供的信息，SQL注入是一种代码注入技术，用于攻击数据驱动的应用程序。在应用程序中，如果没有做恰当的过滤，则可能使得恶意的SQL语句被插入输入字段中执行（例如将数据库内容转储给攻击者）。[2]SQL注入是因为解释器将传入的数据当成命令执行而导致的。预编译是用于解决这个问题的一种方法。和普通的使用流程不同，预编译将一次查询通过两次交互完成，第一次交互发送查询语句的模板，由后端的SQL引擎进行解析为AST或Opcode，第二次交互发送数据，代入AST或Opcode中执行。因为此时语法解析已经完成，所以不会再出现混淆数据和代码的过程。","cited_answer"))
# print(llm_message(Prompt.QUERY_PROMPT.template, "什么是信息安全？","cited_answer"))
# prompt = answer_relevancy.get_prompts()
# p = {"response_relevance_prompt": asyncio.run(prompt["response_relevance_prompt"].adapt("chinese", llm, True))}
# answer_relevancy.set_prompts(**p)
from chat.Chat import Chat
from evaluate.RagasPipeline import run_pipeline


def ragas_test():
    chat_test = Chat(0)
    df = run_pipeline(chat_test)
    print(df.head())

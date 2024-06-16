from langchain.prompts import PromptTemplate

custom_template = """
        You are a helpful assistant.
        Chat History:
        {chat_history}
        Follow-Up Input: {question}
"""

CUSTOM_QUESTION_PROMPT = PromptTemplate.from_template(custom_template)

from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate

class SummarizerAgent:
    def summarize(self, text):
        llm = OpenAI(temperature=0.3)
        prompt = PromptTemplate.from_template(
            "Summarize this in bullet points:\n{text}"
        )
        return llm(prompt.format(text=text))
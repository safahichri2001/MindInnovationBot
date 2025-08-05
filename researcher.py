# researcher.py

import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, Tool

# ✅ Set your Hugging Face API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# 1. Define the DuckDuckGo Search Tool
search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Useful for answering questions about current events, news, or general web information."
    ),
]

# 2. Initialize the LLM with correct args
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    temperature=0.2,
    model_kwargs={
        "max_new_tokens": 256  # ✅ use max_new_tokens, NOT max_length
    }
)

# 3. Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 4. Define your agent interface
class ResearcherAgent:
    def run_research(self, task):
        return agent.run(task)  # ✅ `run()` works fine for agents

# 5. Optional test run
if __name__ == "__main__":
    researcher = ResearcherAgent()
    result = researcher.run_research("What are the latest breakthroughs in AI?")
    print("\n🧠 Agent's Answer:\n", result)

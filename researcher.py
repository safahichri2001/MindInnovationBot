# researcher.py

from langchain_community.llms import HuggingFaceHub
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, Tool
import os

# If you have a Hugging Face API token, set it as an environment variable:
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_huggingface_token_here"

# 1. Define the web search tool
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Useful for answering questions about current events, news, or general web information."
    ),
]

# 2. Initialize the Hugging Face LLM (using a free model, e.g., google/flan-t5-base)
llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={"temperature": 0.2, "max_length": 256}
)

# 3. Initialize the agent
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

class ResearcherAgent:
    def run_research(self, task):
        return agent.run(task)
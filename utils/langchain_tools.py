

from langchain.agents import initialize_agent, Tool
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_community.llms import OpenAI
search = GoogleSearchAPIWrapper()

def run_web_search(query):
    return search.run(query)

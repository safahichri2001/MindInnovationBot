from utils.langchain_tools import run_web_search

class ResearcherAgent:
    def run_research(self, task):
        results = run_web_search(task)
        return results

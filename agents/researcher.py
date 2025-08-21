from utils.gemini_tools import run_web_search

class ResearcherAgent:
    def execute_task(self, task):
        return run_web_search(task)

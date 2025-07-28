
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.search_tools import basic_google_search, search_pubmed

class ResearcherAgent:
    def run_research(self, task):
        if "startup" in task.lower():
            return basic_google_search(task)
        elif "pubmed" in task.lower() or "research" in task.lower():
            return search_pubmed(task)
        else:
            return basic_google_search(task)

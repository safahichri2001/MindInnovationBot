from agents.planner import PlannerAgent
from agents.researcher import ResearcherAgent
from agents.summarizer import SummarizerAgent
from agents.memory import MemoryAgent
from agents.notifier import NotifierAgent

def run_full_workflow():
    planner = PlannerAgent()
    researcher = ResearcherAgent()
    summarizer = SummarizerAgent()
    memory = MemoryAgent()
    notifier = NotifierAgent()

    tasks = planner.define_tasks()
    all_summaries = []

    for task in tasks:
        result = researcher.run_research(task)
        summary = summarizer.summarize(result)
        memory.store(task, summary)
        all_summaries.append(f"🔹 {task}:\n{summary}\n")

    full_summary = "\n\n".join(all_summaries)
    notifier.notify(full_summary)

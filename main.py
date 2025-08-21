import yaml
from agents.planner import PlannerAgent
from agents.researcher import ResearcherAgent
from agents.summarizer import SummarizerAgent
from agents.memory import MemoryAgent
from agents.notifier import NotifierAgent

def main():
    with open("config/settings.yaml", "r") as f:
        config = yaml.safe_load(f)

    planner = PlannerAgent()
    researcher = ResearcherAgent()
    summarizer = SummarizerAgent()
    memory = MemoryAgent()
    notifier = NotifierAgent()

    tasks = planner.define_tasks(config["COUNTRIES"])
    findings = [researcher.execute_task(task) for task in tasks]
    combined = "\n\n".join(findings)
    summary = summarizer.summarize(combined)

    memory.store(summary)
    notifier.notify(summary)

if __name__ == "__main__":
    main()

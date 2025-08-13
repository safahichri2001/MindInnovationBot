import os
from dotenv import load_dotenv
from agents.planner import PlannerAgent
from agents.researcher import ResearcherAgent
from agents.summarizer import SummarizerAgent

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
00
def main():
    # Initialize agents
    planner = PlannerAgent()
    researcher = ResearcherAgent(API_KEY)
    summarizer = SummarizerAgent(API_KEY)

    # Step 1: Planner decides tasks
    topics = planner.plan()

    # Step 2: Researcher collects data
    data = researcher.fetch_data(topics)

    # Step 3: Summarizer creates insights
    summary = summarizer.summarize(data)

    print("=== MindInnovationBot Summary ===")
    print(summary)

if __name__ == "__main__":
    main()

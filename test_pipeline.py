# test_pipeline.py

from agents.researcher import ResearcherAgent
from agents.summarizer import SummarizerAgent
from agents.memory import MemoryAgent

def test_bot():
    # Step 1: Define a test task
    task = "Search for healthcare news in Qatar from yesterday"

    # Step 2: Run Researcher
    researcher = ResearcherAgent()
    raw_data = researcher.execute_task(task)
    print("\n🔍 Raw Research Output:\n", raw_data)

    # Step 3: Run Summarizer
    summarizer = SummarizerAgent()
    summary = summarizer.summarize(raw_data)
    print("\n📝 Summarized Output:\n", summary)

    # Step 4: Store in Memory
    memory = MemoryAgent()
    memory.store(summary)
    print("\n💾 Summary stored in memory_store.json")

if __name__ == "__main__":
    test_bot()

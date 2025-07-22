from agents.researcher_agent import research_mental_health
from agents.summarizer_agent import summarize_content
from agents.memory_agent import MemoryManager

def main():
    query = "Latest innovations in mental health in MENA region"
    
    print("[1] Searching for information...")
    documents = research_mental_health(query)

    print(f"[2] Found {len(documents)} documents. Summarizing...")
    summary = summarize_content(documents)
    print("\n[3] Summary:\n", summary)

    print("[4] Storing summary in memory...")
    MemoryManager.store(query, summary)

    print("\n✅ Done. You can now use the Notifier agent to share this update.")

if __name__ == "__main__":
    main()

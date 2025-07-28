# test_researcher.py

from researcher import ResearcherAgent

agent = ResearcherAgent()
result = agent.run_research("Recent innovations in medical")
for idx, item in enumerate(result, 1):
    print(f"\nResult {idx}:")
    print(item)
    print("-"*40)
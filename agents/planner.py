
print("Loaded planner.py from:", __file__)

class PlannerAgent:
    def define_tasks(self):
        return [
            "Find top 5 mental health startups in MENA",
            "Fetch recent mental health research (PubMed, arXiv)",
            "Check government mental health policies in MENA",
            "Track innovation funding in the region"
        ]

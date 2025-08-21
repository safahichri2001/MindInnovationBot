class PlannerAgent:
    def define_tasks(self, countries):
        return [f"Search for healthcare news in {country} from yesterday" for country in countries]

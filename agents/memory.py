import json
from datetime import date

class MemoryAgent:
    def __init__(self, path="data/memory_store.json"):
        self.path = path
        self.load_memory()

    def load_memory(self):
        try:
            with open(self.path, "r") as f:
                self.memory = json.load(f)
        except FileNotFoundError:
            self.memory = {}

    def store(self, summary):
        today = str(date.today())
        self.memory[today] = summary
        self.save()

    def retrieve(self, day):
        return self.memory.get(day, None)

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.memory, f, indent=2)

import json
from pathlib import Path

class MemoryAgent:
    def __init__(self, path="memory_store/mem0_store.json"):
        self.path = Path(path)
        self.path.parent.mkdir(exist_ok=True)
        if not self.path.exists():
            self.path.write_text(json.dumps([]))

    def store(self, task, result):
        data = json.loads(self.path.read_text())
        data.append({"task": task, "result": result})
        self.path.write_text(json.dumps(data, indent=2))

    def retrieve_all(self):
        return json.loads(self.path.read_text())

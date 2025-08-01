import json
from pathlib import Path

class MemoryAgent:
    def __init__(self, path="memory_store/mem0_store.json"):
        self.path = Path(path)
        self.path.parent.mkdir(exist_ok=True)
        if not self.path.exists() or not self.path.read_text().strip():
            self.path.write_text(json.dumps([]))

    def store(self, task, result):
        try:
            data = json.loads(self.path.read_text())
        except json.JSONDecodeError:
            data = []
        data.append({"task": task, "result": result})
        self.path.write_text(json.dumps(data, indent=2))

    def retrieve_all(self):
        try:
            return json.loads(self.path.read_text())
        except json.JSONDecodeError:
            return []
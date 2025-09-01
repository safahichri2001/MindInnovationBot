import json
from datetime import date
from pathlib import Path
from typing import Optional


class Mem0:
    def __init__(self, path: str = "data/memory_store.json") -> None:
        self.path = Path(path)
        self.load()

    def load(self) -> None:
        if self.path.exists():
            with self.path.open("r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {}

    def store(self, country: str, summary: str) -> bool:
        today = str(date.today())
        self.memory.setdefault(today, {})
        self.memory[today].setdefault(country, [])

        if summary in self.memory[today][country]:
            print(f"🧠 Duplicate summary for {country} on {today}. Skipping.")
            return False

        self.memory[today][country].append(summary)
        self.save()
        print(f"🧠 Stored new summary for {country} on {today}.")
        return True

    def retrieve(self, day: Optional[str] = None) -> dict:
        day = day or str(date.today())
        return self.memory.get(day, {})

    def save(self) -> None:
        with self.path.open("w") as f:
            json.dump(self.memory, f, indent=2)

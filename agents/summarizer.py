# summarizer.py

from utils.gemini_tools import model  # Adjust the import path if needed

class SummarizerAgent:
    def __init__(self):
        self.model = model

    def summarize(self, text):
        if not text:
            raise ValueError("No text provided for summarization.")
        prompt = f"Summarize this:\n{text}"
        response = self.model.generate_content(prompt)
        return response.text

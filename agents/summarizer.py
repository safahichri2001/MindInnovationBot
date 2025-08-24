from utils.gemini_tools import model  # Adjust the import path if needed

class SummarizerAgent:
    def __init__(self):
        self.model = model

    def summarize(self, text):
        if not text:
            raise ValueError("No text provided for summarization.")
        
        prompt = (
            "Summarize the following healthcare news into 3–5 bullet points. "
            "Each point should be concise, factual, and highlight key developments:\n\n"
            f"{text}"
        )

        response = self.model.generate_content(prompt)
        return response.text

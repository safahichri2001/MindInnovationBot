# summarizer_agent.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class SummarizerAgent:
    def __init__(self, api_key=None):
        # Load Gemini API key
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Missing Gemini API key. Please set GEMINI_API_KEY in your .env file.")
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)

    def summarize(self, text, max_words=150):
        """
        Summarizes the given text into a short, clear version.
        """
        prompt = f"Summarize the following text in under {max_words} words, focusing only on the key facts:\n\n{text}"

        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"[ERROR] Summarization failed: {e}")
            return None


if __name__ == "__main__":
    # Test the summarizer
    summarizer = SummarizerAgent()
    test_text = """
    A Saudi-based startup, MindEase, has raised $2M to develop an AI-powered mental health platform.
    This comes as part of a growing trend in MENA's mental health tech ecosystem.
    The UAE has also launched a national tele-therapy program to increase access to psychological support.
    """
    summary = summarizer.summarize(test_text)
    print("=== Summary ===")
    print(summary)

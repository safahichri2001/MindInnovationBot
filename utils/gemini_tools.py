import google.generativeai as genai

# Directly set your Gemini API key here for testing
api_key = "AIzaSyCUunJ0OAIzSxMh7kUMSxf8SIqmQXllvfw"

if not api_key:
    raise ValueError("Gemini API key is missing.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def summarize_text(text):
    response = model.generate_content(f"Summarize this:\n{text}")
    return response.text

def run_web_search(query):
    response = model.generate_content(f"Search for this and summarize:\n{query}")
    return response.text

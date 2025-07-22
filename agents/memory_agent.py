from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", framework="pt")
print(generator("Hello, I'm an AI agent,", max_length=30))

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def summarize_by_length(text, max_length=200):
    """
    Résume le texte en coupant après un certain nombre de caractères.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def summarize_by_sentences(text, max_sentences=3):
    """
    Résume le texte en gardant les premières phrases.
    """
    sentences = sent_tokenize(text)
    summary = " ".join(sentences[:max_sentences])
    return summary
def run_summarizer():
    text = (
        "Mental health is a growing concern globally. "
        "In the MENA region, many initiatives aim to improve access to care. "
        "Startups are developing innovative solutions, including digital therapy and AI tools. "
        "Governments are starting to fund mental health programs more actively. "
        "Public awareness campaigns have also increased."
    )
    print("▶ Résumé par longueur (100 caractères) :")
    print(summarize_by_length(text, max_length=100))
    print("\n" + "-"*60)
    print("▶ Résumé par phrases (2 phrases) :")
    print(summarize_by_sentences(text, max_sentences=2))
    print("\n" + "-"*60)
    print("▶ Résumé par phrases (5 phrases, tout le texte) :")
    print(summarize_by_sentences(text, max_sentences=5))
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
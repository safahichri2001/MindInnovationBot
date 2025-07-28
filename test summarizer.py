from summarizer_agent import summarize_by_length, summarize_by_sentences

text = (
    "Mental health is a growing concern globally. "
    "In the MENA region, many initiatives aim to improve access to care. "
    "Startups are developing innovative solutions, including digital therapy and AI tools. "
    "Governments are starting to fund mental health programs more actively. "
    "Public awareness campaigns have also increased."
)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("▶ Résumé par longueur (100 caractères) :\n")
    f.write(summarize_by_length(text, max_length=100) + "\n")
    f.write("\n" + "-"*60 + "\n")
    f.write("▶ Résumé par phrases (2 phrases) :\n")
    f.write(summarize_by_sentences(text, max_sentences=2) + "\n")
    f.write("\n" + "-"*60 + "\n")
    f.write("▶ Résumé par phrases (5 phrases, tout le texte) :\n")
    f.write(summarize_by_sentences(text, max_sentences=5) + "\n")
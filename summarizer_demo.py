import os
from summarizer_agent import summarize_by_sentences, summarize_by_length
from utils.logger import log

def run_summarizer(input_dir="data/raw", output_dir="data/summaries"):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f:
                text = f.read()

            log(f"🔍 Résumé de {filename}")
            summary = summarize_by_sentences(text, max_sentences=3)

            out_file = os.path.join(output_dir, filename.replace(".txt", "_summary.txt"))
            with open(out_file, "w", encoding="utf-8") as out:
                out.write(summary)
            log(f"✅ Résumé enregistré : {out_file}")
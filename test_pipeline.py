# test_pipeline.py

from agents.summarizer import SummarizerAgent
from agents.memory import MemoryAgent

# Manually curated headlines for each country (replace with dynamic fetch later)
news_sources = {
    "Qatar": [
        {
            "title": "Ministry closes two food establishments for violating health regulations",
            "link": "https://thepeninsulaqatar.com/article/21/08/2025/ministry-closes-two-food-establishments-for-violating-health-regulations",
            "content": "The Ministry of Public Health closed two food outlets due to insect infestations and unlicensed operations, reaffirming its commitment to food safety."
        },
        {
            "title": "Qatar’s healthcare sector transformation under Vision 2030",
            "link": "https://oxfordbusinessgroup.com/reports/qatar/2025-report/health-chapter/",
            "content": "Qatar is integrating mental health, digitalization, and medical tourism into its healthcare strategy, aiming for universal coverage and innovation."
        }
    ],
    "Saudi Arabia": [
        {
            "title": "Saudi Crown Prince launches national blood donation campaign",
            "link": "https://english.alarabiya.net/News/saudi-arabia/2025/08/22/saudi-crown-prince-launches-national-blood-donation-campaign",
            "content": "Mohammed bin Salman initiated a nationwide blood donation campaign to promote voluntary participation and healthcare self-sufficiency."
        },
        {
            "title": "Cross-border heart transplant saves Saudi child",
            "link": "https://www.gulftoday.ae/news/2025/08/21/brain-dead-donor-in-abu-dhabi-saves-saudi-childs-life",
            "content": "A Saudi child received a life-saving heart transplant using a donor organ from the UAE, showcasing regional medical cooperation."
        }
    ],
    "UAE": [
        {
            "title": "UAE evacuates 155 patients from Gaza for urgent medical care",
            "link": "https://www.msn.com/en-ae/news/other/following-presidents-directives-uae-conducts-urgent-medical-evacuation-for-patients-their-families-from-gaza/ar-AA1KTypm",
            "content": "Under presidential directives, the UAE evacuated patients from Gaza, providing treatment across national hospitals."
        },
        {
            "title": "15 Emiratis to be honoured at Health Awards 2025",
            "link": "https://www.gulftoday.ae/news/2025/08/21/15-emiratis-to-be-honoured-at-health-awards-2025",
            "content": "The UAE’s largest healthcare recognition platform will honour 15 Emirati professionals for excellence in clinical care and innovation."
        }
    ]
}

def test_bot():
    summarizer = SummarizerAgent()
    memory = MemoryAgent()

    for country, articles in news_sources.items():
        print(f"\n🌍 {country} Healthcare News:\n")
        digest = ""

        for article in articles:
            summary = summarizer.summarize(article["content"])
            digest += f"📰 [{article['title']}]({article['link']})\n{summary}\n\n"
            memory.store(f"{country}: {summary}")

        print(digest)

if __name__ == "__main__":
    test_bot()

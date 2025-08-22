# agents/researcher.py
import feedparser

class ResearcherAgent:
    def get_updates(self, country):
        if country == "Qatar":
            rss_url = "https://thepeninsulaqatar.com/rss"
        elif country == "Saudi Arabia":
            rss_url = "https://www.arabnews.com/rss"
        else:
            return "No source available."

        feed = feedparser.parse(rss_url)
        articles = []

        for entry in feed.entries:
            if "health" in entry.title.lower() or "medical" in entry.summary.lower():
                articles.append(f"{entry.title}\n{entry.summary}")

        return "\n\n".join(articles[:5]) if articles else "No recent healthcare news found."

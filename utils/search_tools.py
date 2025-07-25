import requests
from bs4 import BeautifulSoup

# Basic Google search using scraping (optional fallback)
def basic_google_search(query, num_results=5):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for g in soup.find_all('div', class_='tF2Cxc')[:num_results]:
        title = g.find('h3')
        link = g.find('a')['href']
        if title and link:
            results.append({"title": title.text, "link": link})
    
    return results

# Search PubMed API (NCBI E-Utilities)
def search_pubmed(query, max_results=5):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    res = requests.get(base_url, params=params)
    id_list = res.json()["esearchresult"]["idlist"]
    
    # Fetch summaries
    summaries_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    summary_params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "json"
    }
    summary_res = requests.get(summaries_url, params=summary_params)
    return summary_res.json()

# Example startup info from Crunchbase or AngelList (if you use API)
# Placeholder
def search_startups_in_mena():
    # You can later use real APIs like Crunchbase
    return [
        {"name": "O7 Therapy", "country": "Egypt", "sector": "Mental Health"},
        {"name": "Shezlong", "country": "Egypt", "sector": "Teletherapy"},
    ]

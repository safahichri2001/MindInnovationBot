# researcher.py

def basic_google_search(query, num_results=5):
    from googleapiclient.discovery import build
    api_key = "AIzaSyCagRleP2abdVsOeSoYKtTLUoNTNnpjK34"
    cse_id = "e7055ac0a55a247c6"
    service = build("customsearch", "v1", developerKey=api_key)
    try:
        params = {
            'q': query,
            'cx': cse_id,
            'num': num_results
        }
        res = service.cse().list(**params).execute()
        items = res.get("items", [])
        if not items:
            return [{
                'title': 'No results found',
                'link': '',
                'snippet': 'No results were returned for your query.',
                'source': ''
            }]
        results = []
        for item in items:
            results.append({
                'title': item.get("title", "No Title"),
                'link': item.get("link", ""),
                'snippet': item.get("snippet", ""),
                'source': item.get("displayLink", "")
            })
        return results
    except Exception as e:
        return [{
            'title': 'Error',
            'link': '',
            'snippet': f'An error occurred: {e}',
            'source': ''
        }]

def search_pubmed(query, max_results=5):
    # Placeholder: returns fake results
    return [f"Fake PubMed result {i+1} for '{query}'" for i in range(max_results)]

class ResearcherAgent:
    def run_research(self, task):
    def run_research(self, task, num_results=5, sort_by_date=True):
        # You can expand this logic to parse keywords for more advanced routing
        if "pubmed" in task.lower() or "research" in task.lower():
            return search_pubmed(task, max_results=num_results)
        else:
            return basic_google_search(task, num_results=num_results, sort_by_date=sort_by_date)
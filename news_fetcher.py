import http.client
import json

SERPER_API_KEY = '850a5eeb2702f4764a38d57cfa7d84bc8e3035d2'

def fetch_news(query, num_articles=5):
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response_data = json.loads(data.decode("utf-8"))
    print(f"Response Data: {response_data}")
    
    articles = []
    if 'organic' in response_data:
        for item in response_data['organic'][:num_articles]:
            articles.append({
                'title': item.get('title', 'No title'),
                'link': item.get('link', 'No link')
            })
    if 'topStories' in response_data:
        for item in response_data['topStories'][:num_articles - len(articles)]:
            articles.append({
                'title': item.get('title', 'No title'),
                'link': item.get('link', 'No link')
            })
    
    return articles

if __name__ == "__main__":
    news = fetch_news("AAPL")
    if news:
        for article in news:
            print(article['title'], article['link'])
    else:
        print("No news articles found.")

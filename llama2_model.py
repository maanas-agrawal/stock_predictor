from transformers import pipeline

def analyze_sentiment(articles):
    sentiment_pipeline = pipeline('sentiment-analysis')
    sentiments = []
    for article in articles:
        title = article['title']
        sentiment = sentiment_pipeline(title)[0]
        sentiments.append({'title': title, 'sentiment': sentiment})
    return sentiments

if __name__ == "__main__":
    articles = [
        {"title": "Apple stock soars after record-breaking quarter"},
        {"title": "Apple faces legal challenges in Europe"}
    ]
    sentiments = analyze_sentiment(articles)
    for sentiment in sentiments:
        print(sentiment)

import streamlit as st
from news_fetcher import fetch_news
from llama2_model import analyze_sentiment

st.title('Custom Stock Predictor')

query = st.text_input('Enter stock ticker or company name:', 'AAPL')
if st.button('Fetch News'):
    articles = fetch_news(query)
    if articles:
        st.subheader('News Articles')
        for article in articles:
            st.markdown(f"[{article['title']}]({article['link']})")
        
        sentiments = analyze_sentiment(articles)
        st.subheader('Sentiment Analysis')
        for sentiment in sentiments:
            st.write(f"**{sentiment['title']}**: {sentiment['sentiment']['label']} (Score: {sentiment['sentiment']['score']:.2f})")
    else:
        st.write('No news articles found. Please check your API key and network connection.')

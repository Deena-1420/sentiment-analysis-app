import streamlit as st
from transformers import pipeline

# Load pre-trained sentiment-analysis model using CPU
sentiment_model = pipeline("sentiment-analysis", device=-1)

def predict_sentiment(text):
    result = sentiment_model(text)
    sentiment = result[0]['label']
    score = result[0]['score']
    return sentiment, score

# Streamlit UI
st.title("Real-Time Sentiment Analysis")
st.subheader("Enter your text to get sentiment analysis:")

user_input = st.text_area("Input Text")

if st.button("Analyze Sentiment"):
    if user_input:
        sentiment, score = predict_sentiment(user_input)
        st.success(f"Sentiment: {sentiment}")
        st.info(f"Confidence Score: {score:.2f}")
    else:
        st.warning("Please enter some text to analyze.")


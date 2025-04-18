# app_ui.py
import streamlit as st
from transformers import pipeline

# Load sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

# UI
st.title("Real-Time Sentiment Analysis")
st.write("Enter a sentence to analyze its sentiment:")

user_input = st.text_area("Text Input", height=150)

if st.button("Analyze"):
    if user_input.strip():
        result = sentiment_model(user_input)[0]
        sentiment = result['label']
        score = result['score']
        st.write(f"### Sentiment: {sentiment}")
        st.write(f"### Confidence: {score:.2f}")
    else:
        st.warning("Please enter some text to analyze.")

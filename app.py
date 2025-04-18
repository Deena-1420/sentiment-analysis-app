import streamlit as st
import joblib
import re

# Load the model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Function to clean the text
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\S+', '', text)  # Remove @mentions
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    return text.lower()

# Function to predict sentiment
def predict_sentiment(text):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return "Positive 😊" if prediction == 1 else "Negative 😞"

# Streamlit UI
st.title('Sentiment Analysis Web App')
st.write("Enter a text to predict the sentiment.")

# User input
user_input = st.text_area("Text for Sentiment Prediction")

if st.button("Predict Sentiment"):
    if user_input:
        sentiment = predict_sentiment(user_input)
        st.write(f"The predicted sentiment is: {sentiment}")
    else:
        st.write("Please enter some text to analyze.")


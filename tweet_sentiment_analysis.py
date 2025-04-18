import tweepy
from transformers import pipeline

# Replace these with your actual credentials
consumer_key = "4ap9lDugZjWUmi9Pe4M5l2579"
consumer_secret = "TJjTMBYPtV9cBqKOvpCXrOzedVe6qtSbiV1CU8dACJRUV8Vb6Z"
access_token = "1414521383200059392-1DS0CyXhL027MCrleQi1vcrwB4OtbE"
access_token_secret = "XIaIz3cPQMNJnzNFaeKzsAim0m8yrO7NF39AAZZBd8jXy"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Load sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

# Function to predict sentiment
def predict_sentiment(text):
    result = sentiment_model(text)
    sentiment = result[0]['label']
    score = result[0]['score']
    return sentiment, score

# Analyze and print sentiment for a tweet
def analyze_tweet_sentiment(tweet):
    sentiment, score = predict_sentiment(tweet.text)
    print("🔹 Tweet:", tweet.text)
    print(f"🔸 Sentiment: {sentiment} (Score: {score:.2f})")
    print("-" * 50)

# Stream Listener using Tweepy v4
class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if tweet.referenced_tweets is None:  # Avoid retweets
            analyze_tweet_sentiment(tweet)

# Replace with your Bearer Token
bearer_token = "AAAAAAAAAAAAAAAAAAAAABLS0gEAAAAA8Nr4dO0%2BQo8kGFyUPYU0cJmjP2I%3DOTwYbtraSsbewez9wMMC3kJpzSwz2ENCuFCfrG4LavrdLm8UV6"

# Start streaming
stream = MyStream(bearer_token)
stream.add_rules(tweepy.StreamRule("love OR hate OR happy OR sad"))  # Filter keywords
print("🎯 Starting tweet sentiment stream...")
stream.filter(tweet_fields=["text"])



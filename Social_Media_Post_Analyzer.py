import re
from textblob import TextBlob

def count_words(text):
    words = text.split()
    return len(words)

def find_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

def determine_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def analyze_social_media_post(post):
    print("Social Media Post Analysis:")
    print("Text:", post)
    word_count = count_words(post)
    print("Number of words:", word_count)
    hashtags = find_hashtags(post)
    print("Hashtags:", hashtags)
    sentiment = determine_sentiment(post)
    print("Sentiment:", sentiment)

# Example usage:
social_media_post = "Great day at the beach! #sunny #beachday"
analyze_social_media_post(social_media_post)

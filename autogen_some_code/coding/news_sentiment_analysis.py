# filename: news_sentiment_analysis.py

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Step 1: Fetch the webpage content
response = requests.get('https://www.example.com/news')
content = response.text

# Step 2: Extract headlines from the webpage
soup = BeautifulSoup(content, 'html.parser')
headlines = [headline.text for headline in soup.find_all('h1')]

# Step 3: Perform sentiment analysis on each headline
sentiment_scores = []
for headline in headlines:
    blob = TextBlob(headline)
    sentiment_scores.append(blob.sentiment.polarity)

# Step 4: Calculate the overall sentiment of the top news articles
overall_sentiment = sum(sentiment_scores) / len(sentiment_scores)

# Step 5: Output the headlines and their sentiment scores
for i in range(len(headlines)):
    print(f"Headline: {headlines[i]}")
    print(f"Sentiment Score: {sentiment_scores[i]}")
    print()

print(f"Overall Sentiment: {overall_sentiment}")
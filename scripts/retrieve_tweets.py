import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

# Load Twitter API keys from .env
load_dotenv()
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Authenticate
client = tweepy.Client(bearer_token=bearer_token)

# Updated query for municipal issues in Johannesburg
query = "(#servicedelivery OR #municipality OR #eskom OR #citypower OR #joburgwater) Johannesburg -is:retweet lang:en"

def get_tweets(query, max_results=500):
    tweets = []
    for tweet in tweepy.Paginator(client.search_recent_tweets,
                                  query=query,
                                  tweet_fields=['author_id', 'created_at', 'text'],
                                  max_results=100).flatten(limit=max_results):
        tweets.append({
            'id': tweet.id,
            'author_id': tweet.author_id,
            'created_at': tweet.created_at,
            'text': tweet.text
        })
    return pd.DataFrame(tweets)

if __name__ == "__main__":
    df = get_tweets(query)
    df.to_csv('data/raw_twitter_data.csv', index=False)
    print(f"Saved {len(df)} tweets to data/raw_twitter_data.csv")

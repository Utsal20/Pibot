import os
import tweepy
# codes.py contains authentication tokens
from codes import *
# scrape_releases.py contains the scrape_episodes() function
from scrape_releases import *

def tweet(tweet_text):
    """Tweets to timeline
    Args:
        tweet_text: formatted text that is to be tweeted
    """
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    api.update_status(tweet_text)

if __name__ == '__main__':
    tweet_text = scrape_episodes()
    
    if tweet_text is not None:
        tweet(tweet_text)

from os import access
import tweepy
import time
import datetime


consumer_key = "yYa55vJbJ6BklwPyE6ad3qGCB"
consumer_secret = "16xhyn8CD2BpRXPO9BVLYf4Ew0Omoz4fB0Urr5z9mndFvRaOuH"
access_token = "872514074625449984-G8fOgKmBp97YFbSnaYObYOtR7gGtwTF"
access_token_secret = "PXVcrq0skuzm4ScP0jIw9CeTva1tsyCdcxpGlINs1kGzv"


auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)


api = tweepy.API(auth)


def twitter_bot(hashtag, delay):
    while True:
        print(f"\n{datetime.datetime.now()}\n")

        for tweet in tweepy.Cursor(api.search_tweets, q=hashtag, rpp=10).items(10):
            try:
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]

                print("id: "+str(tweet_id))
                print("text: "+str(tweet_id))

                api.retweet(tweet_id)
            except tweepy.errors.TweepyException as error:
                print(error)

        time.sleep(10)


twitter_bot("luminol", 10)

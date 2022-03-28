from os import access
import tweepy
import time
import datetime


consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


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


twitter_bot("#luminol", 10)

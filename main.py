from os import access
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)


api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("No Error")
except:
    print("Error")

api.update_status("Insert your message here")

from os import access
import tweepy

# consumer_key = "yYa55vJbJ6BklwPyE6ad3qGCB"
# consumer_secret = "16xhyn8CD2BpRXPO9BVLYf4Ew0Omoz4fB0Urr5z9mndFvRaOuH"
# access_token = "872514074625449984-G8fOgKmBp97YFbSnaYObYOtR7gGtwTF"
# access_token_secret = "PXVcrq0skuzm4ScP0jIw9CeTva1tsyCdcxpGlINs1kGzv"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKpmawEAAAAAd1rZ0iqUio12MfsfjyN5lssCIEI%3DOXz4TYGsGmIe6X8LvAxVgY7nfKG1T2SH4QCZypxoS9Q8NpMtxd"


auth = tweepy.OAuth2BearerHandler(bearer_token)


api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Everything Works")
except:
    print('Something went wrong')

api.update_status("Kya chal raha hain bhai bros")

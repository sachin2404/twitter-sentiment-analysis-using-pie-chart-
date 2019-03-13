import tweepy
from textblob import TextBlob

consumer_key = "xIXYf8RVbFI13bLazq1gx5tyh"
consumer_secret ="Jx6SMAPGheKv8NzeYQEu2SPIjspqFMYRUXEDO2hIbpyKoLLYcK"

access_token ="3052936344-JwuH5XkGlG6XR32TlEPCKsV3HWE1liTPIQjW1jK"
access_token_secret ="W72NmBqjNaliIzjlmcRHmnf4oFbwjIzezg3B9uyP8NZ7u"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = tweepy.Cursor(api.search, q="Infosys", lang="en", result_type="recent").items(200)
count=0
for tweet in public_tweets:
     print(tweet.text)
     analysis = TextBlob(tweet.text)
     print(analysis.sentiment)
     count=count+1


print(count)

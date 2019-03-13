import tweepy
from textblob import TextBlob

consumer_key = ""
consumer_secret =""

access_token =""
access_token_secret =""

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

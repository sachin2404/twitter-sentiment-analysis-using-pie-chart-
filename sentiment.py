# use search text as q.
#you can make function to do this task.
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

consumer_key = "xIXYf8RVbFI13bLazq1gx5tyh"
consumer_secret ="Jx6SMAPGheKv8NzeYQEu2SPIjspqFMYRUXEDO2hIbpyKoLLYcK"

access_token ="3052936344-JwuH5XkGlG6XR32TlEPCKsV3HWE1liTPIQjW1jK"
access_token_secret ="W72NmBqjNaliIzjlmcRHmnf4oFbwjIzezg3B9uyP8NZ7u"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def percentage(uper, lower):
    return 100*float(uper)/float(lower)

public_tweets = tweepy.Cursor(api.search, q="infosys", lang="en", result_type="recent").items(100)
count=0
positive=0
negative=0
nutral=0
polarity=0
for tweet in public_tweets:
     analysis = TextBlob(tweet.text)
     polarity +=analysis.sentiment.polarity
     if(analysis.sentiment.polarity==0):
         nutral += 1
     elif(analysis.sentiment.polarity<0.00):
         negative += 1
     elif(analysis.sentiment.polarity>0.00):
         positive += 1

positive=percentage(positive,100)
negative=percentage(negative,100)
nutral=percentage(nutral,100)

labels=['[positive]', '[negative]','[nutral]']
sizes=[positive,negative,nutral]
colors=['yellowgreen',"gold","red"]
chart=plt.pie(sizes,labels=labels, startangle=90, autopct='%.2f%%',shadow=True)
plt.title("[How people are reacting on {} by analysing tweets]".format("Infosys"))
plt.axis("equal")
plt.tight_layout()
plt.show()


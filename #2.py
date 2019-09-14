import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''


access_token = ''

access_token_secret = ''



#authenticate with twitter , basically login with code

auth = tweepy.OAuthhandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)




""" sentiment analysis is the process of extracting 
and understanding human feelings from data.

API lets you access a serers internal functionality 
like twitter  ,right from your app"""
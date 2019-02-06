# Coding challenge #2.

# import dependencies
import tweepy
from textblob import TextBlob

consumer_key = "BDKT8ysWP1on2dCLVJblQfKkg"
consumer_secret = "LkktmELrslMiX2PEuNa71O3G2v1XXbVl66GWBUugTTa0bAB1MJ"

access_token = "826432687242088448-lQJyOx9QHe9wBrrYOcR7S2D2FpoGcpm"
access_token_secret = "eZTDlmBho2FOi4tQwvNENKPhgkal8STdpVdmUwVuj3aUx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

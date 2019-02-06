# Coding challenge #2.

# import dependencies
import tweepy, csv
from textblob import TextBlob

# define topic of research
topic = 'Trump'

# Keys for the API
consumer_key = "BDKT8ysWP1on2dCLVJblQfKkg"
consumer_secret = "LkktmELrslMiX2PEuNa71O3G2v1XXbVl66GWBUugTTa0bAB1MJ"
access_token = "826432687242088448-lQJyOx9QHe9wBrrYOcR7S2D2FpoGcpm"
access_token_secret = "eZTDlmBho2FOi4tQwvNENKPhgkal8STdpVdmUwVuj3aUx"

# Connecting to the API + authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Searching for tweets...
public_tweets = api.search(topic)

# Opening CSV file
with open('search_results.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Writing the header of the CSV table
    writer.writerow(['Tweet', 'Polarity', 'Subjectivity'])
    # For every tweet found, extract the text, analyze it and write it to the table, 
    # along with the polarity and subjectivity
    for tweet in public_tweets:
        tweet_text = tweet.text
        analysis = TextBlob(tweet_text).sentiment
        writer.writerow([tweet_text, analysis.polarity, analysis.subjectivity])
        
csv_file.close()

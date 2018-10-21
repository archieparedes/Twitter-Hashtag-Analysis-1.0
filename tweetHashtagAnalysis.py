import tweepy
import csv

from config import consumer_key, consumer_secret, access_token, access_token_secret
from pprint import pprint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def hashAnalysis(hashtag):
    data = []
    for tweet in tweepy.Cursor(api.search, q = hashtag, rpp = 50).items(50):
        try: # this handles unknown characters. i.e emojis
            if(tweet.text[:2] == 'RT'): # eliminates third part retweet application 
                pass
            else:
                if(tweet.text not in data):
                    data.append(tweet.text)
        except: 
            pass
            
    with open('tweets.csv','w', encoding='UTF-8', newline='\n') as csvArchive:
        writer=csv.writer(csvArchive)
        writer.writerow(data)
        writer.close()
    return data # returns a list
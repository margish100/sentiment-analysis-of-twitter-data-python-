import re
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
from tweepy import OAuthHandler
from textblob import TextBlob
from collections import Counter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QCheckBox, QDialog
from PyQt5.QtGui import QIcon

class TwitterClient(object):
	'''
	Generic Twitter Class for sentiment analysis.
	'''
	def __init__(self):
		
		
		consumer_key = 'mxV8L8W1DRFjw3gpA86BJaBy3'
		consumer_secret = 'lhQUNsaw5bSo7PTHxkEA420mOJ1LlMsH5uajqIkESIoNOacLV1'
		access_token = '970572423627026433-y81HY08KhtS1KGhizaENRhKXioQ4kro'
		access_token_secret = 'F4kt07nCQEwX9QAUVW5NEgoZT5pKkrQZH2wZW6jIlU8bV'

		
		try:	
			self.auth = OAuthHandler(consumer_key, consumer_secret)	
			self.auth.set_access_token(access_token, access_token_secret)
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def clean_tweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def get_tweet_sentiment(self, tweet):
		
		
		analysis = TextBlob(self.clean_tweet(tweet))
		
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def get_tweets(self, query, count = 10):
		
		tweets = []
		try:
			fetched_tweets = self.api.search(q = query, count = count)
			for tweet in fetched_tweets:
				parsed_tweet = {}
				parsed_tweet['text'] = tweet.text
				
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
				if tweet.retweet_count > 0:
					
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
			return tweets

		except tweepy.TweepError as e:
			
			print("Error : " + str(e))

def run_sentiment(query, count):
    api = TwitterClient()
    tweets = api.get_tweets(query,count)
    #print(dir(tweets[0]))
    #print(tweets[0].id)
    #print(tweets[0].geo)

    """Ex = ['rahul gandhi', 'iphonex', 'trump', 'ipl20', 'narendra modi']
    query = input("Enter the subject for Sentiment analysis \n")
    number = input("Provide the tweet count \n")
    results = api.search(
            lang="en",
            q=query + " -rt",
            count=number,
            result_type="recent")"""
    
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    print("\n\nPositive tweets:")
    for tweet in ptweets[:20]:
        print(tweet['text'])

    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    print("\n\nNegative tweets:")
    for tweet in ntweets[:20]:
        print(tweet['text'])

    
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))

    netweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    print("Neutral tweets percentage: {} %".format(100*len(netweets)/len(tweets)))


    """tp = pd.Series(data= tweet['ptweets'].values, index = tweets['date'])
    #tn = pd.Series(data= tweet['ntweets'].values, index = tweets['date'])

    #tp.plot(figsize=(16,4), label = "+ve tweets", color = "blue", legend =True)
    #tn.plot(figsize =(16,4) ,label = "-ve tweets", color = "red", legend = True)

    t =tweets.groupby('sentiment')
    t.size().plot(kind='bar')"""

    colors = ['green', 'red', 'grey']
    sizes = [format(100*len(ptweets)/len(tweets)), format(100*len(ntweets)/len(tweets)),format(100*len(netweets)/len(tweets))]
    labels = 'Positive', 'Negative', 'Neutral'
    plt.pie(x=sizes, shadow=True, colors=colors, labels=labels, startangle=90)
    plt.title("sentiment analusis of tweets")
    plt.show()
        
if __name__ == "__main__":
   
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    run_sentiment('Donald Trump',100)

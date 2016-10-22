import tweepy
import csv
from tweepy import Stream
from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
	csvWriter=csv.writer(open('tweets.csv','a'))
        csvWriter.writerow([status.created_at,status.text.encode('utf-8')])
 	return True
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_token = "ACCESS TOKEN"
access_token_secret = 'ACCESS TOKEN SECRET'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

listener = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, listener)
stream.filter(track=['#TaylorSwift'])

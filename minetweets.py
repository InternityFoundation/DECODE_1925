import tweepy
import csv
import pandas as pd
import time
####input your credentials here
consumer_key='sjLBPjB31EaFIPQZ5CDozB6dB'
consumer_secret='ca6D6uS4NOETT3jM8wlLziiPhdHCgUd9DqJRk8ilfToVI2ZRnq'
access_token='1110779810601680897-ssFy8MsJ12pt195IdeF1bExDMp8FXM'
access_token_secret='XSECLrzWSSZIQnaYJLHaRCeFuqo44yElbSFMUekSi0MOv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('twts4.txt', 'a')
#Use csv Writer
#csvWriter = csv.writer(csvFile)
i=0
slp=0
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
#csvFile.write('[')
while True:
    try:
        for tweet in tweepy.Cursor(api.search,q="ElectionResults2019",count=100,lang="en").items():
            i+=1
            print (i)
            csvFile.write(str(tweet._json)+'\n')
    except Exception as e:
        print(e)
        if (slp<=900):
            time.sleep(slp)
            slp+=60
            continue
        i=100000
        break
    slp=0
    if (i>=100000):
        break
    #csvWriter.writerow(tweet)
#csvFile.write(']')

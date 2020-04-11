import tweepy
import time

consumer_key='poh31SG7rqmyy4fnLC3Dq8swr'
consumer_secret='xcDP6esc92q5UxZqqVhybxOXzPDCsj7rD3uu1ZReXNq22HZOvW'
access_token='952834660584706048-r03B9uN7bcgKQ7aNRwfHWQYGvWB0v94'
access_token_secret='TCq5nvL8pEzYZZkum1alJInylMbcvzZqiysTFqadVaW0M'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

import pandas as pd

df=pd.read_csv('users1.csv',header=None)

df.columns=['id','handle','followers']
#print(df.head())
usrs=list(df['id'])
#print(usrs)
folls=[]
#print(api.show_friendship(source_id=207809313,target_id=1015365007))


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
import csv
slp=0
#nt=[40839292,59414975,19489239,46638111,18373968,166122648]
f2=open('followings.csv','a')
for i in usrs[147:285]:
#i=usrs[31]
    #print(i)
    with open('followers0.csv','w') as f1:
        writer1=csv.writer(f1)
        writer2=csv.writer(f2)
        f=[]
        l=[]
        for j in usrs:
            if i is not j:
                while True:
                    #
                    try:
                        print(i,j)
                        if api.show_friendship(source_id=i,target_id=j)[0].followed_by:
                            f.append(j)
                            print(f)
                        if api.show_friendship(source_id=i,target_id=j)[0].following:
                            l.append(j)
                            #print(f)
                    except Exception as e:
                        print(e)
                        if (slp<=900):
                            time.sleep(slp)
                            slp+=60
                            continue
                        break
                    slp=0
                    break
        #f.append(i)
        #writer.writerow(list(i))
                    #time.sleep(5)
        writer1.writerow(f)
        writer2.writerow(l)
        folls.append(f)
        print(i)

print(folls)


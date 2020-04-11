import json,ast

tweets=[]

with open('twts4.txt','r') as f:
    while True:
        t=f.readline()
        if (not t):
            break
        tweets.append(ast.literal_eval(t))

print(len(tweets))

ids=[]

#print(len(tweets))

class User:
    def __init__(self,id,name,fllwr):
        self.id=id
        self.name=name
        self.fllwr=fllwr
users=[]
for tweet in tweets:
    u=User(tweet['user']['id'],tweet['user']['screen_name'],tweet['user']['followers_count'])
    if (u.id not in ids and tweet['user']['verified']==1):
        users.append(u)
        ids.append(tweet['user']['id'])

    if ('retweeted_status' in tweet.keys()):
        u=User(tweet['retweeted_status']['user']['id'],tweet['retweeted_status']['user']['screen_name'],tweet['retweeted_status']['user']['followers_count'])
        if (u.id not in ids and tweet['retweeted_status']['user']['verified']==1) :
            users.append(u)
            ids.append(tweet['retweeted_status']['user']['id'])

            
#users=list(set(users))
print(len(users))
import operator

users.sort(key=operator.attrgetter('fllwr'),reverse=1)

import csv

with open('users1.csv', 'w') as f:
    writer = csv.writer(f)
    for u in users:
        writer.writerow([u.id,u.name,u.fllwr])

print(users[1].id,users[1].name,users[1].fllwr)
import os
os.system('spd-say "your program has finished"')

# import pandas as pd
# labels=['ID','Handle','#Followers']
# df=pd.DataFrame.from_records(users)
# print(df.head())
# with open('retUsrs.txt','w') as f:
#     for u in range(len(users)):
#         f.write(str(users[u])+' ')
#         f.write(str(usrname[u])+' ')
#         f.write(str(fllwrCnt[u])+'\n')
#
# print(len(users))
#
# print(json.dumps(tweets[0],indent=2))


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


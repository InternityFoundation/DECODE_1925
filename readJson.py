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

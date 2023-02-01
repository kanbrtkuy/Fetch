import sys
#import numpy as np
import pandas as pd

#earn_points=5000
earn_points = sys.argv[1]
if earn_points == "" :
    print("input error!")
    exit(1)
earn_points = int(earn_points)
df = pd.read_csv("transactions.csv")
#sort by time stamp
df = df.sort_values(axis=0, by='timestamp', ascending=True)
df_size = len(df)
#find the points avlue which is < 0，deduct from the earliest until used all of the points
for i in range(0,df_size) :
    payer = df.iloc[i, 0]
    points = df.iloc[i, 1]
    if points < 0 :
        df.iloc[i, 1] = 0
        for j in range(0, df_size) :
            #print("points=",points)
            if df.iloc[j, 0] == payer :
                AA= 0 - points
                if df.iloc[j, 1] >= AA :
                    df.iloc[j, 1] = df.iloc[j, 1] - AA
                    break
                else :
                    points = df.iloc[j, 1] - AA
                    df.iloc[j, 1] = 0
#print(df)
for i in range(0,df_size) :
    payer = df.iloc[i, 0]
    points = df.iloc[i, 1]
    if points <= earn_points :
        earn_points = earn_points - points
        df.iloc[i, 1] = 0
    else :
        points = points - earn_points
        earn_points = 0
        df.iloc[i, 1] = points
        break
if earn_points != 0 :
    print("points is not enough")
    exit(1)
df_sum = df.groupby('payer').agg({"points":sum})
#convert to dictionary {'points':{'DANNON': 1000, 'MILLER COORS': 5300, 'UNILEVER': 0}}
df_dict = df_sum.to_dict()
#print {'DANNON': 1000, 'MILLER COORS': 5300, 'UNILEVER': 0}
for i in df_dict.values() :
    print(i)

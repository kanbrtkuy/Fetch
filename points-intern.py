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
#print(df)
df_sum = df.groupby('payer').agg({"points":sum})
df_sum = df_sum.to_dict()
for i in df_sum.values() :
    df_sum_dict = i
#print(df_sum_dict)
#sort by time stamp
df = df.sort_values(axis=0, by='timestamp', ascending=True)
df_size = len(df)
#print(df_size)
for i in range(0,df_size) :
    payer = df.iloc[i, 0]
    points = df.iloc[i, 1]
    if df_sum_dict[payer] >= points :
        l_points = points
    else :
        l_points = df_sum_dict[payer]
    if l_points <= earn_points :
        l_points_tmp = l_points
        earn_points = earn_points - l_points
        df.iloc[i, 1] = 0
    else :
        l_points_tmp = earn_points
        l_points = l_points - earn_points
        earn_points = 0
        df.iloc[i, 1] = l_points
        break
    df_sum_dict[payer] = df_sum_dict[payer] - l_points_tmp
    if df_sum_dict[payer] == 0 :
        for j in range(i+1, df_size) :
            if df.iloc[j, 0] == payer :
                df.iloc[j, 1] = 0
if earn_points != 0 :
    print("points is not enough")
    exit(1)
df_sum = df.groupby('payer').agg({"points":sum})
#convert to dictionary data type {'points':{'DANNON': 1000, 'MILLER COORS': 5300, 'UNILEVER': 0}}
df_dict = df_sum.to_dict()
#print {'DANNON': 1000, 'MILLER COORS': 5300, 'UNILEVER': 0}
for i in df_dict.values() :
    print(i)


#Please excute this file following the approach in readme.txt

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

#sort the file by time stamp
df = df.sort_values(axis=0, by='timestamp', ascending=True)
df_size = len(df)

for i in range(0,df_size) :
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
#convert to dictionary type, ie. {'points':{'DANNON': 1000, 'MILLER COORS': 5300, 'UNILEVER': 0}}
df_dict = df_sum.to_dict()
#print the result, {'DANNON': 1000, 'MILLER COORS': 5300, 'UNILEVER': 0}
for i in df_dict.values() :
    print(i)


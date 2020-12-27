#================================ ###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/nabeel/Downloads/input.csv')
df = pd.Series(df['Series'])

for i in range(df.size):
     a = df.iloc[i]
     r = 2020 - a
     for i in range(df.size):
         if(r == df.iloc[i]):
             print(r)
             print(a)
             print(r * a)
             break
         break

df1 = pd.Series([1721,979,366,299,675,1456])
df = pd.read_csv('/home/nabeel/Downloads/input.csv')
df = pd.Series(df['Series'])


for i in range(df.size):
    x = df.iloc[i]
    a = 2020 - x
    for i in range(df.size):
        y = df.iloc[i]
        b = a - y
        for i in range(df.size):
            z = df.iloc[i]
            c = b - z
            if(c == 0):
                print(x)
                print(y)
                print(z)
                print(x * z * y)

def sum():
    for i in range(df.size):
        x = df.iloc[i]
        a = 2020 - x
        for i in range(df.size):
            y = df.iloc[i]
            b = a - y
            for i in range(df.size):
                z = df.iloc[i]
                c = b - z
                if(c == 0):
                 print(x)
                 print(y)
                 print(z)
                 print(x * z * y)
                 return












import pandas as pd
from datetime import datetime

df = pd.read_csv("../resources/wetterdaten.csv")
#print(df)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
#print('otto')
#print(df)
#cutdf = df[(df['Timestamp'] > '2023-10-12 14:30:01') & (df['Timestamp'] < '2023-10-12 16:30:01')]
#print('otto')
#df = df[(df['Timestamp'] > '2023-10-09 22:30:01') & (df['Timestamp'] < '2023-10-12 11:30:0')]
#print(df)
#df.to_csv('resources/filtered.csv')


df = df.dropna()
df.to_csv('resources/filtered.csv')
print(df)
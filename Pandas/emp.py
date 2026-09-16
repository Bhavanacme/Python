import pandas as pd
df=pd.read_csv("bank.csv")
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.columns)
print(df.shape)
print(df.info())


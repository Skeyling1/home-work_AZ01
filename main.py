import pandas as pd

df = pd.read_csv('aminoacids.csv')

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

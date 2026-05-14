import pandas as pd

df = pd.read_csv('movies.csv')
print(df)

print(df[df['rating'] > 8.0])
print(df['rating'].mean())
print(df[['title', 'review']])
print(df.sort_values('rating', ascending=False))

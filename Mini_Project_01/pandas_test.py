import pandas as pd
movies = [
    {'title': 'The Matrix', 'genre': 'Sci-Fi', 'rating': 9.0},
    {'title': 'The Avengers', 'genre': 'Action', 'rating': 10.0},
    {'title': 'The Notebook', 'genre': 'Romance', 'rating': 3.5},
    {'title': 'Inception', 'genre': 'Sci-Fi', 'rating': 8.8},
    {'title': 'Titanic', 'genre': 'Romance', 'rating': 7.8}]

df = pd.DataFrame(movies)   
print(df[df['rating'] < 8.0])   
print(df[['title', 'rating'] ])  
print(df[df['title', 'review']])
print(df.sort_values('rating', ascending=False))



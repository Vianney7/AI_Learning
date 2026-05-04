def get_rating(movie):
    rating = input('What rating would you give ' + movie + '? (1-10) ')
    return float(rating)    

rating1 = get_rating('The Matrix')
rating2 = get_rating('The Avengers')
rating3 = get_rating('The Notebook')

movies = [
    {'title': 'The Matrix', 'rating': rating1},
    {'title': 'The Avengers', 'rating': rating2},
    {'title': 'The Notebook', 'rating': rating3}
]

for movie in movies:
    if movie['rating'] >= 8.0:
        print(movie['title'] + ': Must watch! ⭐')
    elif movie['rating'] >= 6.0:
        print(movie['title'] + ': Worth watching 🎬')
    else:
        print(movie['title'] + ': Skip it ❌')
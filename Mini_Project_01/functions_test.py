

def get_rating(movie):
    rating = input('What rating would you give ' + movie + '? (1-10) ')
    return float(rating)    

rating1 = get_rating('The Matrix')
rating2 = get_rating('The Avengers')
rating3 = get_rating('The Notebook')

ratings = [rating1, rating2, rating3]

for rating in ratings:
    if rating >= 8.0:
        print('This movie is a must watch! ⭐')
    elif rating >= 6.0:
        print('This movie is okay. 🎬')
    else:
        print('This movie is not recommended. ❌')           

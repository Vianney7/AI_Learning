from transformers import pipeline
classifier = pipeline('sentiment-analysis')

movies = [
    {'title': 'The Matrix', 'genre': 'Sci-Fi', 'rating': 9.0},
    {'title': 'The Avengers', 'genre': 'Action', 'rating': 10.0},
    {'title': 'The Notebook', 'genre': 'Romance', 'rating': 3.5},
    {'title': 'Inception', 'genre': 'Sci-Fi', 'rating': 8.8},
    {'title': 'Titanic', 'genre': 'Romance', 'rating': 7.8}
]

def show_recommendations(movies):
    for movie in movies:
        if movie['rating'] >= 7.0:
            print(movie['title'] + ': Must watch! ⭐')

def add_review():
    movie = input('Enter movie name: ')
    review = input('Write your review: ')
    result = classifier(review)
    label = result[0]['label']
    confidence = round(result[0]['score'] * 100, 1)
    file = open('tracker.txt', 'a')
    file.write(movie + ' - ' + review + ' - ' + label + ' (' + str(confidence) + '%)\n')
    file.close()
    print('✅ Review saved!')

print('\n🎬 Movie Tracker')
print('----------------')
print('1. See recommendations')
print('2. Add a review')

choice = input('\nEnter your choice (1 or 2): ')

if choice == '1':
    show_recommendations(movies)
elif choice == '2':
    add_review()
else:
    print('Invalid choice!')
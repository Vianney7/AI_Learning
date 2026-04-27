
from transformers import pipeline

print('Loading AI model...')
classifier = pipeline('sentiment-analysis')

movies = [
    {'title': 'The Matrix', 'review': 'An absolute masterpiece!'},
    {'title': 'The Avengers', 'review': 'Too long and boring.'},
    {'title': 'Avatar', 'review': 'Stunning visuals and great story!'},
    {'title': 'The Notebook', 'review': 'Dull and predictable.'},
    {'title': 'Terminator 2', 'review': 'One of the best action movies ever!'}
]

print('\n🎬 AI Movie Recommendations:')
for movie in movies:
    result = classifier(movie['review'])
    if result[0]['label'] == 'POSITIVE':
        print('✅ Watch: ' + movie['title'] + ' - ' + movie['review'])
    else:
        print('❌ Skip: ' + movie['title'] + ' - ' + movie['review'])
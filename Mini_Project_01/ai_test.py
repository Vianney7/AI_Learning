from transformers import pipeline

print('Loading AI model...')
classifier = pipeline('sentiment-analysis')

sentences = [
    'I love watching movies!',
    'This film was terrible.',
    'The Avengers is an amazing movie!',
    'I really enjoyed the ending',
    'The special effects were disappointing.',
    'Vianney loves learning python!'
]

for sentence in sentences:
    result = classifier(sentence)
    print(sentence + ' - ' + result[0]['label'] + ' (' + str(round(result[0]['score'] * 100, 1)) + '% confident)')
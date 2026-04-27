from transformers import pipeline

print('Loading AI model...')
classifier = pipeline('sentiment-analysis')

print('\n🎬 AI Movie Review Analyser')
print('---------------------------')

while True:
    review = input('\nEnter a movie review (or type quit to exit): ')
    
    if review.lower() == 'quit':
        print('Goodbye! 🎬')
        break
    
    result = classifier(review)
    label = result[0]['label']
    confidence = round(result[0]['score'] * 100, 1)
    
    if label == 'POSITIVE':
        print('✅ POSITIVE review! (' + str(confidence) + '% confident)')
    else:
        print('❌ NEGATIVE review! (' + str(confidence) + '% confident)')
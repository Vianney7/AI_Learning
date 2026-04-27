from transformers import pipeline

print('Loading AI model...')
classifier = pipeline('sentiment-analysis')

print('\n🎬 AI Movie Review Saver')
print('------------------------')

while True:
    movie = input('\nEnter movie name (or quit to exit): ')
    
    if movie.lower() == 'quit':
        print('Goodbye! Reviews saved! 🎬')
        break
    
    review = input('Enter your review: ')
    result = classifier(review)
    label = result[0]['label']
    confidence = round(result[0]['score'] * 100, 1)
    
    # Save to file
    file = open('reviews.txt', 'a')
    file.write(movie + ' - ' + review + ' - ' + label + ' (' + str(confidence) + '%)\n')
    file.close()
    
    print('✅ Review saved!')
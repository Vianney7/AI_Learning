sentiments = []
confidences = []
import pandas as pd
from transformers import pipeline

classifier = pipeline('sentiment-analysis') 

def analyze_review(review):
    result = classifier(review)
    label = result[0]['label']
    confidence = round(result[0]['score'] * 100, 1)
    return label, confidence    

print('🎬 AI Movie Review Analyser')
df = pd.read_csv('movies.csv')
print(df)

for index, row in df.iterrows():
    label, confidence = analyze_review(row['review'])
    sentiments.append(label)
    confidences.append(confidence)

df['sentiment'] = sentiments
df['confidence'] = confidences

print('\n🤖 AI Analysis Results:')
print(df)

df.to_csv('movies_analysed.csv', index=False)
print('\n✅ Saved to movies_analysed.csv!')
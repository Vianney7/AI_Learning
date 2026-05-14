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
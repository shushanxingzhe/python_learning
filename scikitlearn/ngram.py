import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer


js = [
    'This is the first sentence',
    'This is the second sentence,Is there any problem',
    'This is the third sentence',
]

review_df = pd.DataFrame(js)

bow_converter = CountVectorizer(token_pattern='(?u)\\b\\w+\\b')
bigram_converter = CountVectorizer(ngram_range=(2,2), token_pattern='(?u)\\b\\w+\\b')
trigram_converter = CountVectorizer(ngram_range=(3,3), token_pattern='(?u)\\b\\w+\\b')

bow_converter.fit(js)
words = bow_converter.get_feature_names()
bigram_converter.fit(js)
bigram = bigram_converter.get_feature_names()
trigram_converter.fit(js)
trigram = trigram_converter.get_feature_names()
print (len(words), len(bigram), len(trigram))

print(words)
print(bigram)
print(trigram)
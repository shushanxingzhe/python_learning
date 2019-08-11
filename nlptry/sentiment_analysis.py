from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
# import nltk
# nltk.download('movie_reviews')

paragraph = '''
Watching godzilla was probably one of the most insulting two hours of my life. The movie was terrible. Bad acting performance to all the characters. Personally, i hate this movie more than anything you could possibly imagine. Poor storyline and pure garbage from start to finish !! this movie is the worst piece of trash to come out of this year. To all of you, save your money !!
'''
review = TextBlob(paragraph)

if(review.detect_language() != 'en'):
    review = review.translate(to="en")

print(review)


print(review.sentiment)


blob = TextBlob(review.string, analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)


import gensim.models.tfidfmodel
import jieba.analyse.textrank
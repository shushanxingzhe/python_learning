from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer as WL
import nltk
wl = WL()
porter = PorterStemmer()

input = 'I want to check my order 19080600979414538195'
input = 'It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms'

nltk_tokens = nltk.word_tokenize(input)
tokens = []
for token in nltk_tokens:
       token = wl.lemmatize(token)
       token = porter.stem(token)
       tokens.append(token)

proInput = ' '.join(tokens)
print(proInput)





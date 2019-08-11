import re
from nltk.corpus import treebank
from nltk import stem

stemmer = stem.PorterStemmer()

orig = []
stemmed = []
for item in treebank.fileids()[:3]:
    for (word, tag) in treebank.tagged_words(item):
        orig.append(word)
        stemmed.append(stemmer.stem(word))

# Convert the results to a string, and word-wrap them.
results = ' '.join(stemmed)
results = re.sub(r"(.{,70})\s", r'\1\n', results+' ').rstrip()

# Convert the original to a string, and word wrap it.
original = ' '.join(orig)
original = re.sub(r"(.{,70})\s", r'\1\n', original+' ').rstrip()

# Print the results.
print('-Original-'.center(70).replace(' ', '*').replace('-', ' '))
print(original)
print('-Results-'.center(70).replace(' ', '*').replace('-', ' '))
print(results)
print('*'*70)
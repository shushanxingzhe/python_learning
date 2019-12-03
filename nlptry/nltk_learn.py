from nltk import tag, tokenize, chunk


sent = tokenize.word_tokenize("At least nine tenths of the students passed.")
tagged_sent = tag.pos_tag(sent)

tree = chunk.ne_chunk(tagged_sent)

tree.draw()

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
print(stop)


import nltk
from nltk import CFG
groucho_grammar = CFG.fromstring("""
                                S -> NP VP
                                PP -> P NP
                                NP -> Det N | Det N PP | 'I'
                                VP -> V NP | VP PP
                                Det -> 'an' | 'my'
                                N -> 'elephant' | 'pajamas'
                                V -> 'shot'
                                P -> 'in'
                                """)
sent = 'I shot an elephant in my pajamas'
sent = nltk.word_tokenize(sent)
parser = nltk.ChartParser(groucho_grammar)

trees = parser.parse(sent)
for tree in trees:
    print(tree)


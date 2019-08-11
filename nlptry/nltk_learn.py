from nltk import tag, tokenize, chunk


sent = tokenize.word_tokenize("At least nine tenths of the students passed.")
tagged_sent = tag.pos_tag(sent)

tree = chunk.ne_chunk(tagged_sent)

tree.draw()

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
print(stop)



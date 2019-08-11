import nltk
sentence = """
But Google is starting from behind. The company made a late push into hardware, and Apple Siri, available on iPhones, and Amazon Alexa software, which runs on its Echo and Dot devices, have clear leads in consumer adoption.
"""
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)
ne = nltk.chunk.ne_chunk(tagged)
print(ne)
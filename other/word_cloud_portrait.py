"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(path.dirname(__file__))

# Read the whole text.
text = open(path.join(d, 'data/english_words.txt')).read()

alice_mask = np.array(Image.open(path.join(d, "data/alice_mask.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,stopwords=stopwords)

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "data/alice.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.show()
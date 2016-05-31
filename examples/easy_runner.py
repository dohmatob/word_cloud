#!/usr/bin/env python2
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

import sys
from os import path
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
in_filename = path.abspath(sys.argv[1]) if len(sys.argv) > 1 else (
    path.join(d, "constitution.txt"))
with open(in_filename) as fp:
    text = fp.read()

# generate word-cloud and take relative word frequencies into account,
# lower max_font_size
import matplotlib.pyplot as plt
stopwords = STOPWORDS.copy()
map(stopwords.add, ["Subject", "Area", "Subject", "Entered",
                    "Abstract", "paper", "available", "primary", "author",
                    "show", "id", "bid", "title", "authors", "using",
                    "one", "two"])
wordcloud = WordCloud(max_font_size=40, relative_scaling=.8, max_words=200,
                      stopwords=stopwords, random_state=0).generate(text)
plt.figure()
plt.imshow(wordcloud, aspect="auto")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
#image = wordcloud.to_image()
#image.show()

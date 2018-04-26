import nltk
import random
import re

file = open('sherlock.txt', 'r',  encoding="utf8")
ref = file.read().strip()

file.close()

ref = re.sub(' +', ' ',ref)
ref = re.sub(r"[\n]*", "", ref)

words = [x for x in ref.split(' ') if not (x.isdigit())]

print(words[:200])

# TEXT = nltk.corpus.gutenberg.words('austen-emma.txt')
# bigrams = nltk.bigrams(TEXT)
# cfd = nltk.ConditionalFreqDist(bigrams)
#
# # pick a random word from the corpus to start with
# word = random.choice(TEXT)
# # generate 15 more words
# for i in range(15):
#     print word,
#     if word in cfd:
#         word = random.choice(cfd[word].keys())
#     else:
#         break
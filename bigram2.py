import nltk.collocations
import nltk.corpus
import collections
from nltk.collocations import *
from nltk import bigrams
import nltk, re, os, csv

# Quran subset
#filename = raw_input('Enter name of file to convert to ARFF with extension, eg. name.txt: ')
file = open('combine.txt', 'r')
stripped = re.sub(r'<[^<]*?>', '', file.read())

# punctuation and numbers to be removed
punctuation = re.compile(r'[-.?!,":;()|0-9]')

# create list of lower case words
word_list = re.split('\s+', stripped.lower())
print 'Words in text:', len(word_list)

words = (punctuation.sub("", word).strip() for word in word_list)
words = (word for word in words if word not in nltk.corpus.stopwords.words('english'))


bgm    = nltk.collocations.BigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(words)
finder.apply_freq_filter(3)
finder.nbest(bgm.pmi, 10)
scored = finder.score_ngrams(bgm.likelihood_ratio)
print scored

# Group bigrams by first word in bigram.                                        
prefix_keys = collections.defaultdict(list)
for key, scores in scored:
   prefix_keys[key[0]].append((key[1], scores))

print prefix_keys[0]

# Sort keyed bigrams by strongest association.                                  
for key in prefix_keys:
   prefix_keys[key].sort(key = lambda x: -x[1])

print prefix_keys[0]

ofile = open('bigrams.csv', 'wb')
mycsv = csv.writer(ofile)

for key in prefix_keys:

    row = [key, str(prefix_keys[key])]
    mycsv.writerow(row)

ofile.close()

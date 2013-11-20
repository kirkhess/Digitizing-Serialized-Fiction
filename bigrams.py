import nltk.collocations
import nltk.corpus
import collections
from nltk.collocations import *
from nltk import bigrams
import nltk, re, os, csv

file = open('combine.txt', 'r')
stripped = re.sub(r'<[^<]*?>', '', file.read())
a = nltk.wordpunct_tokenize(stripped)

bgm    = nltk.collocations.BigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(a)
finder.apply_freq_filter(3)
finder.nbest(bgm.pmi, 10)
scored = finder.score_ngrams(bgm.likelihood_ratio)

# Group bigrams by first word in bigram.                                        
prefix_keys = collections.defaultdict(list)
for key, scores in scored:
   prefix_keys[key[0]].append((key[1], scores))

# Sort keyed bigrams by strongest association.                                  
for key in prefix_keys:
   prefix_keys[key].sort(key = lambda x: -x[1])
   
print 'continued', prefix_keys['continued'][:10]

ofile = open('bigrams.csv', 'wb')
mycsv = csv.writer(ofile)

for key in prefix_keys:

    row = [key, str(prefix_keys[key])]
    mycsv.writerow(row)

ofile.close()

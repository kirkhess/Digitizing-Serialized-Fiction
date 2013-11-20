import re, nltk, os, csv
from nltk.chunk import ne_chunk
from nltk import FreqDist

indir = '/var/www/omeka/archive/files'
ofile = open('wordfreq.csv', 'wb')

mycsv = csv.writer(ofile)
   
file2 = open('combine.txt', 'r')
stripped = re.sub(r'<[^<]*?>', '', file2.read())

# punctuation and numbers to be removed
punctuation = re.compile(r'[-.?!,":;()|0-9]')

# create list of lower case words
#word_list = re.split('\s+', stripped.lower())
word_list = nltk.word_tokenize(stripped.lower())
print 'Words in text:', len(word_list)

words = (punctuation.sub("", word).strip() for word in word_list)
words = (word for word in words if word not in nltk.corpus.stopwords.words('english'))

#a = nltk.word_tokenize(words)
#fw2 = [w for w in a if not w in nltk.corpus.stopwords.words('english')]
voc7 = FreqDist(words)
for word in voc7:
    thepair = word+ ',' + str(voc7[word])
    mycsv.writerow(pair)

file2.close()
ofile.close()

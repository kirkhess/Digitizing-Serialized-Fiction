import re, nltk, os, csv
from nltk.chunk import ne_chunk
from nltk import FreqDist

indir = '/var/www/omeka/archive/files'
ofile = open('nercsv2.csv', 'wb')
namefile = open('names.csv', 'wb')

mycsv = csv.writer(ofile)
mycsv.writerow(['filename', 'tokencount', 'nercount', 'names', 'freq'])

bigfdist = FreqDist()

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
	
        if f.endswith(".txt"):
            file = open(os.path.join(root,f), 'r')
            print f
	    tokencount = 0
            nercount = 0
            
            stripped = re.sub(r'<[^<]*?>', '', file.read())

            # punctuation and numbers to be removed
            punctuation = re.compile(r'[-.?!,":;()|0-9]')

            # create list of lower case words
            word_list = nltk.word_tokenize(stripped)
            print 'Words in text:', len(word_list)

            # create list
            words = (punctuation.sub("", word).strip() for word in word_list)
            words = (word for word in words if word not in nltk.corpus.stopwords.words('english'))

            #a = nltk.word_tokenize(word_list)
            b = nltk.pos_tag(word_list)
            c = nltk.ne_chunk(b,binary=True)
            tokencount = tokencount + len(word_list)
            fdist = FreqDist()
            for x in c.subtrees():
                if x.node == "NE":
                    words = [w[0] for w in x.leaves()]
                    name = " ".join(words)
                    #print name
                    
                    fdist.inc(name)
		    bigfdist.inc(name)
                    nercount = nercount + 1
	    a = [f, tokencount, nercount,fdist.keys(), fdist.values()]
	    print a
            
	    #mycsv = csv.writer(ofile)
            mycsv.writerow(a)

mycsv2 = csv.writer(namefile)
for word in bigfdist:
    thepair = word+ ',' + str(bigfdist[word])
    mycsv2.writerow(thepair)

mycsv.close()
mycsv2.close()
   

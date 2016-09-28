from common import *
import sklearn.feature_extraction.text
from os import listdir
import sys

def tokenizer(text):
    words = stemwords(tokenize(text))
    return words

def filelist(mypath):
    filenames = []
    for f in listdir(mypath):
        filenames.append(mypath + '/' + f)
    return filenames

def getKey(item):
    return item[1]

tfidf = sklearn.feature_extraction.text.TfidfVectorizer(input='filename', analyzer='word', preprocessor=gettext,
                                                        tokenizer=tokenizer, stop_words='english', strip_accents='ascii')

matrix = tfidf.fit(filelist(sys.argv[1]))
tranmatrix = tfidf.transform([sys.argv[2]])

word = tfidf.get_feature_names()
scorelist = []
for col in tranmatrix.nonzero()[1]:
    if tranmatrix[0, col] >= 0.09:
        scorelist.append((word[col], tranmatrix[0, col]))
result = sorted(scorelist, key=getKey, reverse=True)

for i in range(len(result)):
    print result[i][0], format(result[i][1], '.3f')

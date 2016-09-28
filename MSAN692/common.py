import xml.etree.cElementTree as ET
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem import PorterStemmer
import string
import sys
from collections import Counter
import re

def gettext(xmltext):
    """
    Parse xmltext and return the text from <title> and <text> tags.
    """
    tree = ET.fromstring(xmltext)
    result = ""
    for elem in tree.iterfind('title'):
        result += elem.text
    result += " "

    for elem in tree.iterfind('.//text/*'):
        result += elem.text
        result += " "
    return result

def tokenize(text):
    """
    Tokenize text and return a non-unique list of tokenized words
    found in the text. Normalize to lowercase, strip punctuation,
    remove stop words, drop words of length < 3.
    """
    rgx = re.compile("[" + string.punctuation + "0-9\\r\\t\\n]")
    textFull = rgx.sub(" ", text).lower()
    wordList = re.split(" ", textFull)
    wordlist = []
    for word in wordList:
        if len(word) > 2 and word not in ENGLISH_STOP_WORDS:
            wordlist.append(word)
    return wordlist

def stemwords(words):
    """
    Given a list of tokens/words, return a new list with each word
    stemmed using a PorterStemmer.
    """
    words = [PorterStemmer().stem(word).encode("ascii", "ignore") for word in words]
    return words

if __name__=="__main__":
    file = open(sys.argv[1])
    xmltext = file.read()
    file.close()
    text = gettext(xmltext)
    words = stemwords(tokenize(text))
    counts = Counter(words)
    for pair in counts.most_common(10):
        print pair[0], pair[1]
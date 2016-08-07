"""
This script is what created the dataset pickled.

1) You need to download this file and put it in the same directory as this file.
https://github.com/moses-smt/mosesdecoder/raw/master/scripts/tokenizer/tokenizer.perl . Give it execution permission.

2) Get the dataset from http://ai.stanford.edu/~amaas/data/sentiment/ and extract it in the current directory.

3) Then run this script.
"""

dataset_path='/home/asus/Academics/7th Sem/Intro to NLP/project/data/quora/'

import numpy
import cPickle as pkl

from collections import OrderedDict

import glob
import os

from subprocess import Popen, PIPE

# tokenizer.perl is from Moses: https://github.com/moses-smt/mosesdecoder/tree/master/scripts/tokenizer
tokenizer_cmd = ['./tokenizer.perl', '-l', 'en', '-q', '-']


def tokenize(sentences):

    print 'Tokenizing..',
    text = "\n".join(sentences)
    tokenizer = Popen(tokenizer_cmd, stdin=PIPE, stdout=PIPE)
    tok_text, _ = tokenizer.communicate(text)
    toks = tok_text.split('\n')[:-1]
    print 'Done'

    return toks


def build_dict(path,author_to_class):
    sentences = []
    currdir = os.getcwd()
    authors = author_to_class.keys()
    for author in authors:
        cur_author_path = os.path.join(path,author)
        os.chdir(cur_author_path)
        for ff in glob.glob("*.txt"):
            with open(ff, 'r') as f:
                sentences.append(f.readline().strip())
#             print author, ff

    os.chdir(currdir)

    sentences = tokenize(sentences)

    print 'Building dictionary..',
    wordcount = dict()
    for ss in sentences:
        words = ss.strip().lower().split()
        for w in words:
            if w not in wordcount:
                wordcount[w] = 1
            else:
                wordcount[w] += 1

    counts = wordcount.values()
    keys = wordcount.keys()

    sorted_idx = numpy.argsort(counts)[::-1]

    worddict = dict()

    for idx, ss in enumerate(sorted_idx):
        worddict[keys[ss]] = idx+2  # leave 0 and 1 (UNK)

    print numpy.sum(counts), ' total words ', len(keys), ' unique words'

    return worddict


def grab_data(path, dictionary,author_to_class):
    sentences = []
    currdir = os.getcwd()
    authors = author_to_class.keys()
    y_label = []
    for author in authors:
        cur_author_path = os.path.join(path,author)
        os.chdir(cur_author_path)
        for ff in glob.glob("*.txt"):
            with open(ff, 'r') as f:
                sentences.append(f.readline().strip())
                y_label.append(author_to_class[author])
#             print author, ff
    os.chdir(currdir)
    sentences = tokenize(sentences)
    seqs = [None] * len(sentences)
    for idx, ss in enumerate(sentences):
        words = ss.strip().lower().split()
        seqs[idx] = [dictionary[w] if w in dictionary else 1 for w in words]

    return seqs,y_label

def save_author_to_class_dict(author_to_class,csvFile="author.csv"):
    import csv
    f=open(csvFile, "w")
    w = csv.writer(f)
    for key, val in author_to_class.items():
        w.writerow([key, val])
    f.close()
    print "saved the dict"

def load_author_to_class_dict(csvFile="author.csv"):
    import csv
    dict2 = {}
    for key, val in csv.reader(open(csvFile)):
        print key , val
        dict2[key] = int(val)
    return dict2

def create_author_to_class_dict(inputTxt = "authors.txt",outputCsv = "authors.csv"):
    f = open(inputTxt,'r')
    authors = f.readlines()
    authors = [author.strip() for author in authors]
    id_map = zip(authors,range(len(authors)))
    author_to_class= dict(id_map)
    class_to_author = dict((v, k) for k, v in author_to_class.iteritems())
    save_author_to_class_dict(author_to_class,csvFile = outputCsv)


def main():
    # Get the dataset from http://ai.stanford.edu/~amaas/data/sentiment/
    path = dataset_path
    author_csv_file = os.path.join(path,"author.csv")
    author_to_class = load_author_to_class_dict(author_csv_file)
    dictionary = build_dict(os.path.join(path, 'train'),author_to_class)
    train_x, train_y = grab_data(os.path.join(path,"train"),dictionary,author_to_class) 
    test_x, test_y = grab_data(os.path.join(path,"test"),dictionary,author_to_class)
    f = open(os.path.join(path,"quora.pkl"), 'wb')
    pkl.dump((train_x, train_y), f, -1)
    pkl.dump((test_x, test_y), f, -1)
    f.close()
    

    f = open(os.path.join(path,"quora_dict.pkl"), 'wb')
    pkl.dump(dictionary, f, -1)
    f.close()

if __name__ == '__main__':
    main()
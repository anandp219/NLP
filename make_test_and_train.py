import nltk.data
import sys
import os
import glob
from nltk.tokenize import RegexpTokenizer
import shutil

os.mkdir("train")
os.mkdir("test")
with open('writers.txt') as f:
	for line in f:
		author=line.strip()
		os.mkdir("train/"+author)
		os.mkdir("test/"+author)
		files= glob.glob("new_corpus/"+author+"/*.txt")
		print len(files)
		i=10
		s=(int)(0.7*len(files))
		print "train=",s
		for i in range(0,s):
			shutil.copy2(files[i],"train/"+author+"/")
		for j in range(s,len(files)):
			shutil.copy2(files[j],"test/"+author+"/")
			print 'train',j
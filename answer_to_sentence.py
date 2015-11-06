import nltk.data
import sys
import os
import glob
from nltk.tokenize import RegexpTokenizer

sentence_tokenizer = RegexpTokenizer(r'\w+')
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
author_no=0
fe=open('sentence_with_author_no.csv','w')
with open('writers.txt') as f:
	for line in f:
		author=line.strip()
		files= glob.glob("corpus/"+author+"/*.txt")
		for file in files:
			print file
			fp=open(file)
			data=fp.read()
			data=tokenizer.tokenize(data)
#			print data
			for sentence in data:
			#	print sentence
				sentence=sentence.replace("\n","")
				sentence = sentence.replace(","," ")
			#	sent=" ".join((sentence_tokenizer.tokenize(sentence)))
			#	print sent
				
				if len(sentence)>=10 and len(sentence.split(" ")) > 4:
					#print sent
					fe.write(sentence+","+str(author_no)+"\n")	
		author_no=author_no+1
fe.close()

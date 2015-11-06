import nltk.data
import sys
import os
import glob
from nltk.tokenize import RegexpTokenizer

sentence_tokenizer = RegexpTokenizer(r'\w+')
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
author_no=0
os.mkdir("new_corpus")
with open('writers.txt') as f:
	for line in f:
		author=line.strip()
		os.mkdir("new_corpus/"+author+"/")
		files= glob.glob("corpus/"+author+"/*.txt")
		count=1
		for file in files:
			print file
			fp=open(file)
			data=fp.read()
			data=tokenizer.tokenize(data)
#			print data
			answer=""
			for i in range(0,len(data)):
				sentence=data[i]
			 	sentence=sentence.replace("\n","")
			 	sentence = sentence.replace(","," ")
			 	if len(answer)>=500:
			 		wr=open("new_corpus/"+author+"/Answer"+str(count)+".txt",'w')
			 		count=count+1
			 		wr.write(answer)
			 		answer=sentence
			 		wr.close()
			 	else:
			 		answer=answer+" "+sentence
			if len(answer)>=200:
				wr=open("new_corpus/"+author+"/Answer"+str(count)+".txt",'w')
		 		count=count+1
		 		wr.write(answer)
		 		answer=""
		 		wr.close()

			# #	sent=" ".join((sentence_tokenizer.tokenize(sentence)))
			# #	print sent
				
			# 	if len(sentence)>=10 and len(sentence.split(" ")) > 4:
			# 		#print sent
			# 		fe.write(sentence+","+str(author_no)+"\n")	
		author_no=author_no+1
fe.close()

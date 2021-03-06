import json
import urllib
import feedparser,os
import codecs
from bs4 import BeautifulSoup
import shutil
import math
import pickle
import sys

data={}
shutil.rmtree('corpus')
shutil.rmtree('pickle')
os.mkdir("corpus")
os.mkdir("pickle")
author_no=-1
lis=[]
with open('writers.txt','r') as f:
    for line in f:
        line=line.strip()
	os.mkdir("corpus/"+line)
	link="https://www.quora.com/"+line+"/answers/rss"
	author_no=author_no+1
	print author_no
	f=feedparser.parse(link)
	print line +" Answers are being parsed "
	data[line]={}
	answers={}
	for i in range (0,len(f['entries'])):
		answers={}
		#print "Done ==> "+str((i/len(f['entries']))*100)+ "%"
		entry=f['entries'][i]['description']
		soup=BeautifulSoup(entry)
		for div in soup.findAll('a', 'user'):
			div.extract()
		text= soup.get_text()
		text=text[:-22]
		#print text
		if(len(text)<=500):
			#print line
			continue
		text=text.encode('ascii','ignore')
		#print len(text)
		# if(len(text)>=5000):
		# 	fil="corpus/"+line+"/Answer"+str(i+1)+"_part.txt"
		# 	fe=open(fil,'w')
		# 	index=len(text)/2
		# 	while text[index]!= " " and text[index]!= ".":
		# 		index=index+1 
		# 	fe.write(text[:(index)])
		# 	fe.close()
		# 	l=text[:(index)]
		# 	sentences=l.split(". ")
		# 	answers['no_of_sentences']=len(sentences)
		# 	fes=open('sentence.csv','a')
		# 	for i in range(0,len(sentences)):
		# 		wr=sentences[i]+","+str(author_no)+"\n"
		# 		fes.write(wr)
		# 	fes.close()
		# 	z="Answer"+str(i+1)+"_part.txt"			
		# 	answers['key']=z			
		# 	words=l.split(" ")
		# 	answers['no_of_words']=len(words)
		# 	sumi=0
		# 	for word_index in range(0,len(words)):
		# 		lsd=len(words[word_index])
		# 		sumi=sumi+lsd
		# 	avg=float(sumi)/len(words)
		# 	answers['avg_word_length']=avg
		# 	sumi=0
		# 	for word_index in range(0,len(words)):
		# 		lsd=len(words[word_index])
		# 		lsd=(lsd-avg)*(lsd-avg)
		# 		sumi=sumi+lsd
		# 	std=math.sqrt(float(sumi)/len(words))
		# 	answers['standard_dev']=std	
		# 	lis.append(answers)
		# 	text=text[(index):]
		fil="corpus/"+line+"/Answer"+str(i+1)+".txt"
		z="Answer"+str(i+1)+".txt"
		answers['text']=text
		answers['author_no']=author_no
		words=text.split(" ")
		sentences=text.split(". ")
		# fes=open('sentence.csv','a')
		# for i in range(0,len(sentences)):
		# 	wr=sentences[i]+","+str(author_no)+"\n"
		# 	fes.write(wr)
		# fes.close()
	#	answers['no_of_sentences']=len(sentences)
	#	answers['no_of_words']=len(words)
		sumi=0
		for word_index in range(0,len(words)):
			lsd=len(words[word_index])
			sumi=sumi+lsd
		avg=float(sumi)/len(words)
		#answers['avg_word_length']=avg
		sumi=0
		for word_index in range(0,len(words)):
			lsd=len(words[word_index])
			lsd=(lsd-avg)*(lsd-avg)
			sumi=sumi+lsd
		std=math.sqrt(float(sumi)/len(words))
	#	answers['standard_dev']=std
		fe=open(fil,'w')
		lis.append(answers)
		fe.write(text)
		fe.close()
	#data[line]=lis
pickle.dump( lis , open( "pickle/list_"+line+".b", "wb" ) )
print lis

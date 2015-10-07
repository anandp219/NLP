import urllib
import feedparser,os
import codecs
from bs4 import BeautifulSoup
with open('writers.txt','r') as f:
    for line in f:
        line=line.strip()
	os.mkdir(line)
	link="https://www.quora.com/"+line+"/answers/rss"
	f=feedparser.parse(link)
	for i in range (0,len(f['entries'])):
		entry=f['entries'][i]['description']
		soup=BeautifulSoup(entry)
		text= soup.get_text()
		text=text[:-22]
		print text
		if(len(text)<=1000):
			print line
			continue
		text=text.encode('ascii','ignore')
		fil=line+"/Answer"+str(i+1)+".txt"
		fe=open(fil,'w')
		fe.write(text)
		fe.close()

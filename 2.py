import urllib
import feedparser,os
import codecs
from bs4 import BeautifulSoup
with open('writers.txt','r') as f:
    for line in f:
        line=line.strip()
	
	for i in range (1,51):
		link="Answer"+i+".txt"
		with open(link,'r+') as g:
			for line in g:
				

import nltk
nltk.download()
import bs4 as bs
import urllib.request
import re

# scrap the text and put it into article_text
def scrap_article():
	
	scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
	article = scraped_data.read()
	parsed_article = bs.BeautifulSoup(article,'lxml')
	paragraphs = parsed_article.find_all('p')
	article_text = ""

	for p in paragraphs:
	    article_text += p.text
    
	return article_text
 


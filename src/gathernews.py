#Description: Scrape and Summarize News Articles

#import libraries
import nltk
from newspaper import Article

def Input():
	userInput = input("Please enter any keyword(press enter to continue): ")
	return userInput
	

def SearchArticle(url):
	article = Article(url)

	# Do some NLP
	article.download()      #Downloads the link’s HTML content
	article.parse()         #Parse the article
	nltk.download('punkt')  #1 time download of the sentence tokenizer
	article.nlp()           #Keyword extraction wrapper

	#Get the authors,title and summary
	Authors = article.authors
	Title = article.title

	Summary = article.summary

	DocumentArticle(Title, Authors, Summary)

def DocumentArticle(Title, Author, Summary):
	Document = open('news_summary.txt', 'w')
	Document.write(Title + " - " + Author[0])
	Document.write(Summary)
	Document.close()



#Get the article
url1 = 'https://www.washingtonpost.com/technology/2019/07/17/you-downloaded-faceapp-heres-what-youve-just-done-your-privacy/?noredirect=on&utm_term=.1938589d078f'
article = Article(url1)

SearchArticle(url1)
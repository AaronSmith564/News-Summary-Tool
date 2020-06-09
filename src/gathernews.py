#Description: Scrape and Summarize News Articles

#import libraries
import nltk
import newspaper

def Input():
	userInput = input("Please enter any keyword(press enter to continue): ")
	return userInput
	
def SearchCNNArticle(input):
	for CNN_article in cnn_paper.articles:
		#Do some NLP
		try:
			CNN_article.download()      #Downloads the link’s HTML content
			CNN_article.parse()         #Parse the article
		except:
    			continue
		CNN_article.nlp()           #Keyword extraction wrapper
		
		Keywords = CNN_article.keywords
		
		if input in Keywords:
			#Get the authors,title and summary
			Authors = CNN_article.authors
			Title = CNN_article.title
			Summary = CNN_article.summary
			DocumentArticle(Title, Authors, Summary)

def SearchNYTArticle(input):
	for NYT_article in NYTimes_paper.articles:
		#Do some NLP
		try:
			NYT_article.download()      #Downloads the link’s HTML content
			NYT_article.parse()         #Parse the article
		except:
    			continue
		NYT_article.nlp()           #Keyword extraction wrapper
		
		Keywords = NYT_article.keywords
		
		if input in Keywords:
			#Get the authors,title and summary
			Authors = NYT_article.authors
			Title = NYT_article.title
			Summary = NYT_article.summary
			DocumentArticle(Title, Authors, Summary)

def SearchWPArticle(input):
	for WP_article in WP_paper.articles:
		#Do some NLP
		try:
			WP_article.download()      #Downloads the link’s HTML content
			WP_article.parse()         #Parse the article
		except:
    			continue
		WP_article.nlp()           #Keyword extraction wrapper
		
		Keywords = WP_article.keywords
		
		if input in Keywords:
			#Get the authors,title and summary
			Authors = WP_article.authors
			Title = WP_article.title
			Summary = WP_article.summary
			DocumentArticle(Title, Authors, Summary)

def DocumentArticle(Title, Author, Summary):
	Document = open('news_summary.txt', 'w')
	Document.write(Title + " - " + str(Author))
	Document.write(Summary)
	Document.close()



#Get the article

CNN_URL = []
NYT_URL = []
WP_URL = []

cnn_paper = newspaper.build('https://www.cnn.com/', language= 'en', memoize_articles=False, keep_article_html=True)
NYTimes_paper = newspaper.build('https://www.nytimes.com/', language='en', memoize_articles=False, keep_article_html=True)
WP_paper = newspaper.build('https://www.washingtonpost.com/', language='en', memoize_articles=False, keep_article_html=True)
nltk.download('punkt')	    #1 time download of the sentence tokenizer

UserInput = Input()
print("Please wait this will take a while . . . .")

SearchCNNArticle(UserInput)
SearchNYTArticle(UserInput)
SearchWPArticle(UserInput)

print("Fuction Finished, exiting")



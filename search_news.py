from difflib import SequenceMatcher
import newspaper

def search_news(out_db):
    cnn = newspaper.build('http://cnn.com')
    for article in cnn.articles:
    	print(article)
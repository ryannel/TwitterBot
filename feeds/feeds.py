from config import feeds as feedsConfig
from feeds.Article import Article
from logger import logger
import feedparser

def getArticles():
	articles = []
	
	for feedConfig in feedsConfig:
		feed = feedparser.parse(feedConfig['feed'])
		
		if (feed['bozo'] > 0 and len(feed.entries) == 0):
			logger.error('Invalid RSS Feed: {} - {}'.format(feedConfig['name'], feed['bozo_exception']))
			continue
			
		for entry in feed.entries[:feedConfig['limit']]:
			article = Article()
			article.title = entry.title
			article.link = entry.link
			article.source = feedConfig['name']
			
			articles.append(article)
	
	return articles

from dataStore import dataStore
from helpers import scheduler
from generic import utils as genericUtils
from feeds import feeds as feedApi
from reddit import api as redditApi
from logger import logger

modelKey = 'genericPosts'
timekey = 'lastScrapeTime'

def getGenericPosts():
	if scheduler.isTimeToScrape(timekey) == True:
		logger.debug('Scraping for new content')
		genericPosts = scrapeNewGenericPosts()
		saveGenericPostsInDataStore(genericPosts)
		scheduler.setTimeInDataStore(timekey)
	else:
		logger.debug('Using existing content')
		genericPosts = getGenericPostsFromDataStore(modelKey)
	return genericPosts

def scrapeNewGenericPosts():
	newGenericPosts = []
	newGenericPosts = getGenericPostsFromFeeds(newGenericPosts)
	newGenericPosts = getGenericPostsFromReddit(newGenericPosts)
	return newGenericPosts
	
def saveGenericPostsInDataStore(genericPosts):
	genericModel = dataStore.get(modelKey)
	genericModel = genericPosts
	dataStore.set(modelKey, genericModel)
	
def getGenericPostsFromDataStore(modelKey):
	return dataStore.get(modelKey)
	
def getGenericPostsFromFeeds(newGenericPosts):
	blogArticles = feedApi.getArticles()
	for blogArticle in blogArticles:
		genericPost = genericUtils.createGenericPostFromArticle(blogArticle)
		newGenericPosts.append(genericPost)
		
	return newGenericPosts
	
def getGenericPostsFromReddit(newGenericPosts):
	redditPosts = redditApi.getTopPosts()
	for redditPost in redditPosts:
		genericPost = genericUtils.createGenericPostFromRedditPost(redditPost)
		newGenericPosts.append(genericPost)
		
	return newGenericPosts
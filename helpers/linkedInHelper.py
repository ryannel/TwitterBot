from dataStore import dataStore
from helpers import scheduler
from config import linkedIn as linkedInConfig
from logger import logger
import random

modelKey = 'linkedIn'
timerKey = 'lastLinkedInPostTime'

def savePost(post):
	twitterModel = dataStore.get(modelKey)
	
	if twitterModel.get(post.link) == None:
		twitterModel[post.link] = post
		dataStore.set(modelKey, twitterModel)
	
def getPosts():
	return dataStore.get(modelKey)
	
def runLinkedInSchedule(newGenericPosts):
	if scheduler.isTimeToPost(timerKey, linkedInConfig['times']) == True:
		potentialPosts = []
		oldPosts = getPosts()
		for genericPost in newGenericPosts:
			if (oldPosts.get(genericPost.link) == None):
				potentialPosts.append(genericPost)
		
		genericPost = random.choice(potentialPosts)
		linkedInPost = genericPost.generateLinkedInPost()
		scheduler.setTimeInDataStore(timerKey)
		savePost(linkedInPost)
		logger.info('Posting on LinkedIn : {}'.format(linkedInPost.title))
		linkedInPost.post()
		
		if len(potentialPosts) == 0:
			logger.warn('LinkedIn - No new content')
	else:
		logger.debug('LinkedIn worker : waiting')
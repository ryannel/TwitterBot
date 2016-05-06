#!/usr/bin/python

from helpers import genericHelper
from helpers import twitterHelper
from helpers import linkedInHelper
from helpers.SingleInstance import SingleInstance
from logger import logger

instance = SingleInstance()
	
def fetchAndPublishNewPosts():
	
	logger.debug('=================')
	logger.debug('Start Run')
	newGenericPosts = genericHelper.getGenericPosts()
	twitterHelper.runReTweetSchedule()
	twitterHelper.runTweetSchedule(newGenericPosts)
	linkedInHelper.runLinkedInSchedule(newGenericPosts)
	logger.debug('End Run')
	logger.debug('=================')
	
if __name__ == "__main__":
	fetchAndPublishNewPosts()
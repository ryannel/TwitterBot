
from config import twitter as twitterConfig
from helpers import scheduler
from logger import logger
from twitter import api as twitterApi
from twitter import utils as twitterUtils
import random

def runTweetSchedule(newGenericPosts):
	timerKey = 'lastTweetTime'
	
	if scheduler.isTimeToPost(timerKey, twitterConfig['tweetTimes']) == True:
		potentialTweets = []
		
		for genericPost in newGenericPosts:
			if (twitterUtils.isOldTweet(genericPost.link) == False):
				potentialTweets.append(genericPost)
	
		random.shuffle(potentialTweets)
		
		for genericPost in potentialTweets:
			tweet = genericPost.generateTweet()
			if (tweet.getLength() <= 140):
				scheduler.setTimeInDataStore(timerKey)
				logger.info('tweeting : {}'.format(tweet.title))
				twitterUtils.saveTweet(tweet)
				tweet.tweet()
				break
	
		if len(potentialTweets) == 0:
			logger.warn('Twitter - No new content')
				
	else:
		logger.debug('Tweet worker : waiting')
		
def validateRetweet(reTweet, reTweetConfig):
		if twitterUtils.isOldReTweet(reTweet['id']) == True:
			return False
		
		if reTweetConfig.get('minReTweets'):
			if reTweet['retweet_count'] <= reTweetConfig['minReTweets']:
				return False
				
		if reTweetConfig.get('minLikes'):
			if reTweet['user']['favourites_count'] <= reTweetConfig['minFavourites']:
				return False
		
		return True
	
def runReTweetSchedule():
	reTweetConfig = scheduler.getRetweetConfigForCurrentTime()
	if reTweetConfig != False:
		topTweets = twitterApi.search(reTweetConfig['SearchString'], 50, reTweetConfig['ResultType'])
		
		for reTweet in topTweets:
			if validateRetweet(reTweet, reTweetConfig) == True:
				twitterUtils.saveReTweet(reTweet)
				response = twitterApi.reTweet(reTweet['id'])
				
				if response.status_code == 200:
					scheduler.setTimeInDataStore('lastRetweetTime')
					logger.info('retweeting : {}'.format(reTweet['text']))
					return

		logger.debug('ReTweet worker: no matching tweets found')
		
	else:
		logger.debug('ReTweet worker: waiting')
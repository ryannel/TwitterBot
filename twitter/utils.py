from dataStore import dataStore

modelKey = 'twitter'

def saveTweet(tweet):
	twitterModel = getTwitterData()
	
	if twitterModel['tweets'].get(tweet.link) == None:
		twitterModel['tweets'][tweet.link] = tweet
		dataStore.set(modelKey, twitterModel)
		
def saveReTweet(retweet):
	twitterModel = getTwitterData()
	
	if twitterModel['retweets'].get(retweet['id']) == None:
		twitterModel['retweets'][retweet['id']] = retweet
		dataStore.set(modelKey, twitterModel)
		
def getTweets():
	return getTwitterData()['tweets']
	
def getReTweets():
	return getTwitterData()['retweets']
	
def getTwitterData():
	twitterData = dataStore.get(modelKey)

	if twitterData.get('tweets') == None:
		twitterData['tweets'] = {}
		
	if twitterData.get('retweets') == None:
		twitterData['retweets'] = {}
		
	return twitterData
	
def isOldTweet(key):
	oldTweets = getTweets()
	if (oldTweets.get(key) == None):
		return False
	else:
		return True
		
def isOldReTweet(key):
	oldReTweets = getReTweets()
	if (oldReTweets.get(key) == None):
		return False
	else:
		return True 
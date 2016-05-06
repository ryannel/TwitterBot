from dataStore import dataStore
from datetime import timedelta,datetime
from config import twitter as twitterConfig

def getDateTimeFromTime(timeString):
	time = datetime.strptime(timeString,'%H:%M').time()
	return datetime.now().replace(hour=time.hour, minute=time.minute, second=0, microsecond=0)
	
def getTimeFromDataStore(key):
	lastPostTime = dataStore.get(key)
	if lastPostTime == {}:
		return datetime.fromtimestamp(0)
	else:
		return datetime.strptime(lastPostTime,'%Y-%m-%d %H:%M:%S.%f')
		
def setTimeInDataStore(key):
	dataStore.set(key, str(datetime.now()))
		
def isTimeToPost(lastPostKey, configTimes):
	lastPostTime = getTimeFromDataStore(lastPostKey)
	now = datetime.now()
	
	for currentPostTime in configTimes:
		currentPostTime = getDateTimeFromTime(currentPostTime)
		if (lastPostTime <= currentPostTime and currentPostTime <= now):
			return True
	return False
	
def isTimeToScrape(timeKey):
	lastScrapeTime = getTimeFromDataStore(timeKey)
	if lastScrapeTime < datetime.now() - timedelta(days=1):
		return True
	else:
		return False
		
def getRetweetConfigForCurrentTime():
	lastReTweetTime = getTimeFromDataStore('lastRetweetTime')
	retweetConfigs = twitterConfig['retweets']
	now = datetime.now()
	
	for retweetConfig in retweetConfigs:
		currentConfigTime = getDateTimeFromTime(retweetConfig['time'])
		if (lastReTweetTime <= currentConfigTime and currentConfigTime <= now):
			return retweetConfig

	return False
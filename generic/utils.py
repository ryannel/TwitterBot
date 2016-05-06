from generic.GenericPost import GenericPost
from config import reddit as redditConfig
from config import feeds as feedsConfig
import random
import reddit

def createGenericPostFromRedditPost(redditPost):
	generic = GenericPost()
	generic.title = redditPost.title
	generic.link = redditPost.link
	generic.hashtags = getHashtagsForSubreddit(redditPost)
	
	return generic
	
def getHashtagsForSubreddit(redditPost):
	subredditsConfig = redditConfig['subreddits']
	
	for subRedditConfig in subredditsConfig:
		if subRedditConfig['name'] == redditPost.subreddit:
			if (subRedditConfig.get('randomHashtags') == None):
				return subRedditConfig['twitterHashtags']
			else:
				return " ".join(random.sample(subRedditConfig['twitterHashtags'].split(), subRedditConfig['randomHashtags']))
	return ''
	
def createGenericPostFromArticle(article):
	generic = GenericPost()
	generic.title = article.title
	generic.link = article.link
	generic.hashtags = getHashtagsForFeed(article)
	
	return generic
	
def getHashtagsForFeed(article):
	for feedConfig in feedsConfig:
		if feedConfig['name'] == article.source:
			if (feedConfig.get('randomHashtags') == None):
				return feedConfig['twitterHashtags']
			else:
				return " ".join(random.sample(feedConfig['twitterHashtags'].split(), feedConfig['randomHashtags']))
			
	return ''
	

	

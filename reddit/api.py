from reddit.EndPoint import EndPoint
from config import reddit as redditConfig
from reddit import utils

def getTopPosts() :
	endPoint = EndPoint()
	posts = []
	
	subredditsConfig = redditConfig['subreddits']
	
	for subRedditConfig in subredditsConfig:
		response = endPoint.request(subRedditConfig['name'], subRedditConfig['sort'], subRedditConfig['limit'])
		
		for jsonPost in response:
			if(utils.validatePost(jsonPost['data'], subRedditConfig)):
				post = utils.createPostFromJson(jsonPost['data'], subRedditConfig)
				posts.append(post)
	
	return posts
	

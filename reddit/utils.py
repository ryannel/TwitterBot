from urllib.parse import urlparse
from os.path import splitext
from reddit.Post import Post
from config import reddit as redditConfig

blackList = redditConfig['blackList']

def validatePost(post, subRedditConfig):
	validUrl = validateUrl(post['url']) == True
	validScore = post['score'] >= subRedditConfig['minScore']
	over18 = post['over_18'] == subRedditConfig['over18']
	validTitle = validateTitle(post['title'])

	if (validUrl and validScore and over18 and validTitle) :
		return True
	else:
		return False
	
def validateUrl(url):	
	parsed_uri = urlparse(url)
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	ext = splitext(parsed_uri.path)[1]
	
	if domain not in blackList['domains'] and ext not in blackList['extensions']:
		return True
	else:
		return False
		
def validateTitle(title):
	for item in blackList['substrings']:
		if item in title:
			return False
	return True
		
def createPostFromJson(json, config):
	post = Post()
	post.title = json['title']
	post.link = json['url']
	post.subreddit = config['name']
	
	return post
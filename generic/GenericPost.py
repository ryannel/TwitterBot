from twitter.Tweet import Tweet
from linkedIn.Post import Post as LinkedInPost

class GenericPost():
	def __init__(self):
		self.title = None
		self.link = None
		self.hashtags = None
		self.shortLink = None
	
	def generateTweet(self):
		tweet = Tweet()
		tweet.title = self.title
		tweet.link = self.link
		tweet.hashtags = self.hashtags
		tweet.shortLink = self.shortLink
		return tweet
	
	def generateLinkedInPost(self):
		linkedInPost = LinkedInPost()
		linkedInPost.title = self.title
		linkedInPost.link = self.link
		linkedInPost.hashtags = self.hashtags
		linkedInPost.shortLink = self.shortLink
		return linkedInPost
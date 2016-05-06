from logger import logger
import json
from oauth.OAuth1 import OAuth1

client_key = ''
client_secret = ''
callback_uri = 'https://127.0.0.1/callback'

request_token_url = 'https://api.twitter.com/oauth/request_token'
authorization_url = 'https://api.twitter.com/oauth/authorize'
access_token_url = 'https://api.twitter.com/oauth/access_token'

twitterOauth = OAuth1(client_key, client_secret, callback_uri, request_token_url, authorization_url, access_token_url)

def tweet(message):
	session = twitterOauth.getSession()
	
	resourceUrl = 'https://api.twitter.com/1.1/statuses/update.json'
	new_status = {'status': message}
	
	response = session.post(resourceUrl, data=new_status)
	
	if response.status_code != 200:
		logger.error('Twitter Error: {}'.format(response.json()))
		
def search(term, count, resultType):
	session = twitterOauth.getSession()
	
	resourceUrl = 'https://api.twitter.com/1.1/search/tweets.json'
	payload = {
		'q': 			term,
		'lang': 		'en',
		'count': 		count,
		'result_type': 	resultType
	}
	
	response = session.get(resourceUrl, params=payload)
	
	if response.status_code != 200:
		logger.error('Twitter Error: {}'.format(response.json()))
		
	return response.json()['statuses']
		
def reTweet(tweetId):
	session = twitterOauth.getSession()
	
	resourceUrl = 'https://api.twitter.com/1.1/statuses/retweet/{}.json'.format(tweetId)
	payload = {'trim_user': 1}
	
	response = session.post(resourceUrl, data=payload)
	
	if response.status_code != 200:
		logger.error('Twitter Error: {}'.format(response.json()))
		
	return response
	
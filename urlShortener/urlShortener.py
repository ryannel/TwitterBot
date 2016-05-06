from oauth.OAuth2 import OAuth2 
import json
from logger import logger 

client_id = ''
client_secret = ''
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
authorization_base_url = "https://accounts.google.com/o/oauth2/auth"
token_url = "https://accounts.google.com/o/oauth2/token"
refresh_url = 'https://www.googleapis.com/oauth2/v3/token'
scope = ['https://www.googleapis.com/auth/urlshortener']

googleOauth = OAuth2(client_id, client_secret, redirect_uri, authorization_base_url, token_url, refresh_url, scope)

def shorten(longUrl):
	session = googleOauth.getSession()
	post_url = 'https://www.googleapis.com/urlshortener/v1/url'
	payload = {'longUrl': longUrl}
	headers = {'content-type': 'application/json'}
	
	response = session.post(post_url, data=json.dumps(payload), headers=headers)
	
	response = json.loads(response.text)
	
	if response.get('error') == None:
		return response['id']
	else:
		logger.error('Google URL Shortener Error: {}, URL: {}'.format(response['error']['errors'], longUrl))
		return longUrl
	
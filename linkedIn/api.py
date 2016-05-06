from oauth.OAuth2 import OAuth2 
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
from logger import logger
import json

client_id = ''
client_secret = ''
redirect_uri = 'http://127.0.0.1'
authorization_base_url = "https://www.linkedin.com/uas/oauth2/authorization"
token_url = "https://www.linkedin.com/uas/oauth2/accessToken"
headers = {'content-type': 'application/json'}
refresh_url = None
scope = ['w_share']

googleOauth = OAuth2(client_id, client_secret, redirect_uri, authorization_base_url, token_url, refresh_url, scope)

def post(message):
	session = googleOauth.getSession()

	post_url = 'https://api.linkedin.com/v1/people/~/shares?format=json'
	headers = {'content-type': 'application/json'}
	payload = {
				"comment": message,
					"visibility": {
						"code": "anyone"
					}
				}
	
	response = session.post(post_url, data=json.dumps(payload), headers=headers, verify=False)
	
	response = json.loads(response.text)
	
	if response.get('errorCode') == None:
		return response['updateUrl']
	logger.error('LinkedIn Error: {}'.format(response['message']))
	
def getProfile():
	session = googleOauth.getSession()

	post_url = 'https://api.linkedin.com/v1/people/~?format=json'
	
	response = session.get(post_url, headers=headers, verify=False)
	
	response = json.loads(response.text)
	
	if response.get('errorCode') == None:
		return response
	logger.error('LinkedIn Error: {}'.format(response['message']))
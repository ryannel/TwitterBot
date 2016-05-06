import requests
import json
from config import reddit as redditConfig

class EndPoint():
    def __init__ (self):
        self.baseURL = redditConfig['endPoint']['url']
        self.headers = redditConfig['endPoint']['headers']
        
    def request (self, subreddit, sort, limit):
        url = '{0}/r/{1}/new.json?sort={2}&limit={3}'.format(self.baseURL, subreddit, sort, limit)
        response = requests.get(url, headers=self.headers).json()
        return response['data']['children']

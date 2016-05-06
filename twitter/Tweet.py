from twitter import api
from urlShortener import urlShortener
from logger import logger
import random 

class Tweet():
    def __init__ (self):
        self.title = None
        self.link = None
        self.hashtags = None
        self.shortLink = None
        
    def _getTweetFormat(self):
        # 0 = title, 1 = hashtags, 3 = shortlik
        formatArray = [
            '{0} | {1} | {2}',
            '{0} {1} {2}',
            '{0} {1}\n\n{2}',
            '{0}\n\n{1}\n\n{2}',
            '{0}\n\n{1}\n{2}'
        ]
        
        return random.choice(formatArray)
        
    def generate(self):
        self.shortlink = urlShortener.shorten(self.link)
        message = self._getTweetFormat().format(self.title, self.hashtags, self.shortlink)
        return message
        
    def getLength(self):
        return len('{} {}| '.format(self.title, self.hashtags)) + 20
        
    def tweet(self):
        api.tweet(self.generate())
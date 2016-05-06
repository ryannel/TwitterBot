from linkedIn import api as linkedInApi
from urlShortener import urlShortener

class Post():
    def __init__ (self):
        self.title = None
        self.link = None
        self.hashtags = None
        self.shortLink = None
        
    def _getHashTagStringFormat(self):
        hashtags = ''
        if (self.hashtags != ''):
            hashtags = '| {} '.format(self.hashtags)
        return hashtags
        
    def generate(self):
        self.shortlink = urlShortener.shorten(self.link)
        message = '{} {}| {}'.format(self.title, self._getHashTagStringFormat(), self.shortlink)
        return message
        
    def getLength(self):
        return len('{} {}| '.format(self.title, self._getHashTagStringFormat())) + 20
        
    def post(self):
        message = self.generate()
        linkedInApi.post(message)
# Twitter Bot

Generates tweets from blog and forum posts scraped from the web.

Supports:
* Posting to Twitter
* Posting to LinkedIn
* Minifying URLs using Google's URL minifyer
* Scraping posts from Reddit
* Scraping posts from RSS feeds
* Ability to post at configured times
* Random Tweet layouts
* Configurable hash tags and mentions besed on data source
* Auto retweets based on post poularity and content

Developed on python3.4

# Installation
python3 -m pip install --upgrade requests requests_oauthlib feedparser

# Firewall friendly Installation
python3 -m pip install --upgrade --trusted-host pypi.python.org --index-url=http://pypi.python.org/simple/ requests requests_oauthlib feedparser

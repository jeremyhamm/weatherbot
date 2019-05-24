#!/usr/bin/env python
from credentials import *
from bs4 import BeautifulSoup
import tweepy
import urllib.request
import datetime

#Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get high/low temps
url = 'http://www.wpc.ncep.noaa.gov/discussions/hpcdiscussions.php?disc=nathilo&version=0&fmt=reg'   
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
dataarea = soup.find('div', id="printarea")
tempArr = dataarea.findAll('b', text=True)

tempStr = ''
for elm in tempArr:
  tempStr += ''.join(elm.findAll(text=True)) + '\n'

# Get yesterdays date
current = datetime.datetime.now() - datetime.timedelta(days=1)

# Send tweet
tweet = 'Yesterday was ' + str(current.month) + '/' + str(current.day) + '/' + str(current.year) + '\nHigh & Low Temps: ' + '\n' + tempStr
#print(tweet)
api.update_status(tweet)
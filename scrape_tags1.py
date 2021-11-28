# Extract Tags
from bs4 import BeautifulSoup
import requests
import re

from scrapetest import getTitle

html = requests.get('http://www.mikiyakobayashi.com/projects')
bs = BeautifulSoup(html.read(), 'html.parser')

pictureList = bs.find_all('img src')
index = 1
for picture in pictureList:
    print(f'Picture #{index} is {picture}')
    index += 1

""" There's an easy way to scale these for loops, but for redundancy sake I am keeping them separate. """

""" I'm trying to figure out how to shorten the html link so that I can extract the ttle of the photo. """
""" I guess that's where you have to use text processing """
linkList = bs.find_all('a href')
index = 1
for link in linkList:
    print(f'Link #{index} is {link}')
    index += 1

""" Parse the link. """
def linkParser(link):
    str.replace(link, '/', ' ')

    return link


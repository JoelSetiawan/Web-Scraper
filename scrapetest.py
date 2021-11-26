# Simple scraper that takes out the html content of a webpage.
from urllib.request import urlcleanup, urlopen
from urllib.error import HTTPError, URLError
from urllib.error import URLErrors
from bs4 import BeautifulSoup

import requests
import re


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://leeandlie.blogspot.com/2016/04/again-english-lyrics.html')
if title == None:
    print('Title could not be found')
else:
    print(title)


print('It worked!')
scrape_lyrics = BeautifulSoup(html, 'html.parser')
pretty_lyrics = scrape_lyrics.decode(pretty_print=True, eventual_encoding='utf-8', formatter='minimal')
print(pretty_lyrics)
print('\n\n\n\n')



# Simple scraper that takes out the html content of a webpage.
from urllib.request import urlcleanup, urlopen
from urllib.error import HTTPError, URLError
from urllib.error import URLErrors
from bs4 import BeautifulSoup

import requests
import re

try:
# Opening one of my favorite anime song lyrics
    html = urlopen('http://leeandlie.blogspot.com/2016/04/again-english-lyrics.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else: 
    # Program continues.
    print('It worked!')
    scrape_lyrics = BeautifulSoup(html, 'html.parser')
    pretty_lyrics = scrape_lyrics.decode(pretty_print=True, eventual_encoding='utf-8', formatter='minimal')
    print(pretty_lyrics)
    print('\n\n\n\n')
    
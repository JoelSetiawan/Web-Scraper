# Simple scraper that takes out the html content of a webpage.
from urllib.request import urlcleanup, urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# Requests is urllib3, the better version of urllib.
import requests

# Re stands for Regular Expressions
import re

import sys

def getTitle(url):
    try:
        html = requests.get(url)
    except HTTPError as e:
        return None
    finally:
        bs = BeautifulSoup(html.text, 'html.parser')
        title = bs.body.h1
    return title

def main(argv):
    link1 = 'http://leeandlie.blogspot.com/2016/04/again-english-lyrics.html'
    title = getTitle(link1)

    if title == None:
        print('Title could not be found')
    else:
        print(title)

    try: 
        html = urlopen(link1)
    except HTTPError as e:
        print('You got an HTTP error!')
    except AttributeError as e:
        print('You weren\'t able to get the attribute that you wanted')
    finally: 
        bs = BeautifulSoup(html.read(), 'html.parser')
        print('It worked!')
        scrape_lyrics = bs
        pretty_lyrics = scrape_lyrics.decode(pretty_print=True, eventual_encoding='utf-8', formatter='minimal')
        print(pretty_lyrics)
        print('\n\n\n\n')

if __name__ == "__main__":
    main(sys.argv)

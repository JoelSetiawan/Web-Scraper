# Extract Tags
from bs4 import BeautifulSoup
import requests
import re

from scrapetest import getTitle

html = requests.get('http://www.mikiyakobayashi.com/projects')
bs = BeautifulSoup(html.read(), 'html.parser')


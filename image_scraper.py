from bs4 import BeautifulSoup
import re # regex library
import requests # requests that we want to send out.

def getdata(url):
    r = requests.get(url)
    return r.text

htmldata = getdata("https://www.ramenizakayaakira.com/")
# print(f'This is the html\'s data {htmldata}')

soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])


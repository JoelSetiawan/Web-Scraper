from bs4 import BeautifulSoup
import requests

def getdata(url):
    r = requests.get(url)
    return r.text

htmldata = getdata("https://translate.google.com/")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])


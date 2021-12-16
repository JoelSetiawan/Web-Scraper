# Extract Tags
from bs4 import BeautifulSoup

import sys

import requests

import re

""" The plan is to create a web scraper that relies on input from my program, then we expand it to taking in user input, then expand the features
, allowing users to, when searching for it have a trie data structure for autocorrection, and then we expand it to saving the record 
of the data we have scraped onto a file/database, and/or organizes this. """

""" Let's break down my steps 

    1. Learn how BeautifulSoup works
    2. Let People Search for Things they want with the web scraper
        People should be able to write the link of the website they want to scrape
            In the future, create a feature that allows them to choose what html attribute they want to scrape.
    3. Let Myself Search a website for keywords or sentences that I want to scrape
        Potential:
        Job Posting Keywords
        Literature
        Metadata that tells me something has updated
        Notifications on Website Updates

    4. Data Structures and Algorithms I will have to use:
        Binary Search - To Search for Important Stuff
        Knowing how to traverse the BeautifulSoup tree
        LinkedList
        Regular Lists
        Text Processing
        Creating a Database
            Requires A Record Data Structure with Fields for Queries

    Important things to remember
        Code Readibility and Maintainability
        Work on small chunks of the project
        Don't forget the function is the most important aspect
        Automatic means it runs on its own, learn how automatic works.
        Persevere Through, It will get Boring
        Clean your code and writing.

If I try to import another file as a header, python decides to run the whole other file before this file. 
We can scale this requests by allowing the link to come from user input or a file. """


def main(argv):
    html = requests.get('http://www.mikiyakobayashi.com')
    
    SoupObject = BeautifulSoup(html.text, 'html.parser');
    prettifiedSoup = SoupObject.prettify()

    print(f'This is the prettified version of our beautiful soup: ' + prettifiedSoup)

    images = SoupObject.find_all('img')
    print(images)

if __name__ == "__main__":
    main(sys.argv) 

# index = 0
# for picture in pictureList:
#     print(f'Picture #{index} is {picture}')
#     index += 1

# """ There's an easy way to scale these for loops, but for redundancy sake I am keeping them separate. """

# """ I'm trying to figure out how to shorten the html link so that I can extract the ttle of the photo. """
# """ I guess that's where you have to use text processing """
# linkList = bs.find_all('a href')
# index = 1
# for link in linkList:
#     print(f'Link #{index} is {link}')
#     index += 1

# """ Parse the link. """
# def linkParser(link):
#     str.replace(link, '/', ' ')
#     return link


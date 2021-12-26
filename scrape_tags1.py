# Extract Tags
from bs4 import BeautifulSoup

import sys
import requests

import string
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

def wordCounter(string):
    pass

""" Parses list of find_all object """
# Improvement would be to make it so that all attributes are printed out: tag, a href, image, etc.
# Postcondition: none
def parse_list(input_data, name):
    if (input_data):
        index = 0
        for data in input_data:
            index += 1
            print(f'{name} #{index}: {data}')
        print(f'{index} Entries Found for {name}\n')
    else:
    # Formats
        print(f'No Entries Found for {name}\n')
        

def main(argv):
    html = requests.get('http://www.mikiyakobayashi.com')
    
    SoupObject = BeautifulSoup(html.text, 'html.parser');
    prettifiedSoup = SoupObject.prettify()
    # print(f'This is the ugly version of our beautiful soup: {SoupObject}')
    # print(f'This is the prettified version of our beautiful soup: ' + prettifiedSoup)

    images = SoupObject.find_all('img')
    parse_list(images, 'Image')

    # Finds all with the id light
    lightCount = SoupObject.find_all(id='light')
    parse_list(lightCount, '\'Light\'')
    # This doesn't work
    # SoupObject.find_all(class='green')
    # This works
    
    green_classes = SoupObject.find_all(class_ = 'green')
    parse_list(green_classes, '\'Green\' Class')
    # This first returns all ids with watch, and is not useful for finding both id and class.
    green_watch_classes = SoupObject.find_all(id='watch', class_='green')
    parse_list(green_watch_classes, '\'Green\' & \'Watch\' Class')

    # Find all of the words from the text
    text_eyes = SoupObject.find_all(text='eyes')
    parse_list(text_eyes, '\'Eyes\' in Text')

    # Redundant, Pre-Regex way to try and find all Header tags
    all_headers = SoupObject.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    parse_list(all_headers, 'Header')

    # Finds all spans with class green or red.
    green_red_spans = SoupObject.find_all('span', {'class':{'green', 'red'}})
    parse_list(green_red_spans, '\'Green\' & \'Red\' Class')

if __name__ == "__main__":
    main(sys.argv) 

import bs4
from bs4 import BeautifulSoup
from lxml import html
import requests
from urllib.request import urlopen

import bookFinder
from Book import Book

dest = "https://www.goodreads.com/search?utf8=%E2%9C%93&query="


def getInfo(title):
    actual_title = title
    title = title.replace(" ", "+")
    url = dest + title
    result = requests.get(url)
    source = urlopen(url)
    soup = bs4.BeautifulSoup(source, 'html.parser')

    names = soup.find_all('span', {'itemprop': 'name'})[1].text.strip()
    ratings = soup.find('span', {'class': 'minirating'}).text.strip()

    score = ratings[0:4]
    numRatings = ratings[18:len(ratings) - 8]
    author = names
    # cover = bookFinder.getBookCover(title)
    bkFound = Book(actual_title, author, score, numRatings)
    return bkFound

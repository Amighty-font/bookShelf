import requests
from bs4 import BeautifulSoup
import os
import google_images_download


def getBookCover(title):
    from google_images_download import google_images_download  # importing the library

    response = google_images_download.googleimagesdownload()  # class instantiation

    arguments = {"keywords": title,
                 "format": "png",
                 "suffix_keywords": "Book Cover",
                 "output_directory": "coverImages",
                 "limit": 1,
                 "print_urls": True}
    paths = response.download(arguments)


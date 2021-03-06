# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 13:44:26 2019

@author: Root
"""

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all("a")

#print(a_tags)

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))

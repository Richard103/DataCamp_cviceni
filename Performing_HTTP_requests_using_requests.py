# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:36:55 2018

@author: Root
"""

# Import package
import requests

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)

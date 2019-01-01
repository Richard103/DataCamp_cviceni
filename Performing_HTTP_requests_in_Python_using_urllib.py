# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 13:13:49 2018

@author: Root
"""

# Import packages
import urllib as ul

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = ul.Request(url)

# Sends the request and catches the response: response
response = ul.urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()
ul.
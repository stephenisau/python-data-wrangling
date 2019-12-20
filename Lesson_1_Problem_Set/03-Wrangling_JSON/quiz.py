#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This exercise shows some important concepts that you should be aware about:
- using codecs module to write unicode files
- using authentication with web APIs
- using offset when accessing web APIs

To run this code locally you have to register at the NYTimes developer site 
and get your own API key. You will be able to complete this exercise in our UI without doing so,
as we have provided a sample result.

Your task is to process the saved file that represents the most popular (by view count)
articles in the last day, and return the following data:
- list of dictionaries, where the dictionary key is "section" and value is "title"
- list of URLs for all media entries with "format": "Standard Thumbnail"

All your changes should be in the article_overview function.
The rest of functions are provided for your convenience, if you want to access the API by yourself.
"""
import json
import codecs
import requests

URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = { "popular": "",
            "article": ""}

def get_from_file(kind, period):
    """
    This function reads from the current working directory a json file and returns the data
    """
    filename = "popular-{0}-{1}.json".format(kind, period)
    with open(filename, "r") as f:
        return json.loads(f.read())

def pretty_print(data, indent=4):
    """
    This function makes json data more human-readable
    """
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    elif type(data) == list:
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(data)))
    else:
        print(data)

nyTimes = get_from_file('viewed', 1)
print(type(nyTimes))
print(len(nyTimes))
for article in nyTimes:
print(article)
"""
    titles = []
    urls =[]

    for article in data:
        section = article["section"]
        title = article["title"]
        titles.append({section: title})
        if "media" in article:
            for m in article["media"]:
                for mm in m["media-metadata"]:
                    if mm["format"] == "Standard Thumbnail":
                        urls.append(mm["url"])
    return (titles, urls)
    """
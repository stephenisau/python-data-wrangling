#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function

from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
import codecs

datafile = "FL-ATL.html"
datadir = "data"
"""
def open_zip(datadir):
    datadir = os.path.join(datadir, datafile)
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    datadir = os.path.join(datadir, datafile)
    files = os.listdir(datadir)
    return files
"""
def process_all(datadir):
    datadir = os.path.join(datadir, datafile)
    f = codecs.open(datadir, 'r')
    file = f.read()
    return file

def process_file(f):
    # This is example of the datastructure you should return
    # Each item in the list should be a dictionary containing all the relevant data
    # Note - year, month, and the flight data should be integers
    # You should skip the rows that contain the TOTAL data for a year
    # data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #         },
    #         {"courier": "..."}
    # ]
    data = []
    info = {}
    info["courier"], info["airport"] = "ATL", "FL"
    
    with open("{}/{}".format(datadir, f), "r") as html:
        tempDict = dict()
        soup = BeautifulSoup(html)
        table = soup.find('table')
        TRS = table.findAll('tr',class_='dataTDRight')
        for tr in TRS.findAll('td'):
            if 'TOTAL' not in str(tr):
                tempDict['courier'] = info['courier']
                tempDict['airport'] = info['airport']
                tempDict['year'] = int(tr[0].text)
                tempDict['month'] = int(tr[1].text)
                flightDict = dict()
                flightDict['domestic'] = int(tr[2].text.replace(',',''))
                flightDict['international'] = int(tr[3].text.replace(',',''))
                tempDict['flights'] = flightDict
                data.append(tempDict)
    return data


def test():
    print ("Running a simple test...")
#    open_zip(datadir)
    files = process_all(datadir)
    data = []
    for f in files:
        data += process_file(f)
    assert len(data) == 3
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    print ("... success!")

if __name__ == "__main__":
    test()

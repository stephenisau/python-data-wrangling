#!/usr/bin/env python3
"""
Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""
import csv
import os

DATADIR = os.path.dirname(__file__)
DATAFILE = "data/745090.csv"
datafile = os.path.join(DATADIR, DATAFILE)

def parseFile(datafile):
    name = ""
    data = []
    with open(datafile,'r') as f:
        header = f.readline().strip().split(',')
        col_names = f.readline().strip().split(',')
        name += header[1]
        for line in f:
            line = line.strip()

            data_field = {}
            temp_value = line.split(',')
            
            for i, value in enumerate(temp_value):
                data_field[header[i].strip()] = value.strip()
            data.append(data_field)


    # Do not change the line below
    return (name, data)

# def parse_file(datafile):
#     name = ""
#     data = []
#     with open(datafile,'r') as f:
#         header = f.readline().strip().split(',')
#         col_names = f.readline().strip().split(',')
#         name += header[1]
#         for line in f:
#             line = line.strip()

#             temp_value = line.split(',')
            
#             data.append(temp_value)

#     # Do not change the line below
#     return (name, data)

# name, data = parse_file(datafile)
# print(name, data)

def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == '"MOUNTAIN VIEW MOFFETT FLD NAS"'
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()

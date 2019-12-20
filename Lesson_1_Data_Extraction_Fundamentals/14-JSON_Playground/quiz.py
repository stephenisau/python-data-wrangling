"""
Try to answer the following questions with the musicbrainz
1. How many bands named "First Aid Kit"?
2. What is the Begin_Area for Queen?
3. What is the Spanish Alias for Beatles?
4. Nirvana Disambiguation?
5. When was One Direction formed?
"""
import json
import requests
# from musicbrainz import *


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def querySite(url, params, uid='', fmt='json'):
    """
    This function uses the requests library to connect
    to musicbrainz api and returns the data in json format
    """
    params['fmt'] = fmt
    r = requests.get(url + uid, params=params)
    print('requesting ' + str(r.url))
    if r.status_code ==  requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status() 

#params = {'fmt':'json'}
def queryByName(url, params, name):
    """
    This function makes use of the querySite function above and passes 
    a call to the api to return the artist by name
    """
    params['query'] = "artist:" + name
    return querySite(url, params)
#params = {'fmt':'json', 'query':'artist'}

def pretty_print(data, indent=4):
    """
    This function just makes the returned data
    human-readable
    """
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    elif type(data) == list:
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(data)))
    else:
        print(data)


# 1. How many bands named "First Aid Kit"?
"""
#params = {'fmt':'json', 'query':'artist'}
#requesting http://musicbrainz.org/ws/2/artist/?query=artist%3AFirst+Aid+Kit&fmt=json

#pretty_print(query1)
#print(len(query1))
#print(type(query1))
#print("At first glance the answer looks like 4, but let's investigate")

#firstAidKit = query1['artists']
#print("Printing dictionary key => query1['artists']: ")
#pretty_print(firstAidKit)
#print(len(firstAidKit))
#print(type(firstAidKit))
"""
query1 = queryByName(ARTIST_URL, query_type['simple'], "First Aid Kit")
firstAidKit = query1['artists']

count = 0
for item in firstAidKit:
    #print(item['name'])
    if item['name'] == 'First Aid Kit':
        count += 1

#print("1. How many bands named 'First Aid Kit'?\n")        
#print("Number of bands named First Aid Kit: " + count)

#2. What is the Begin_Area for Queen?
"""
print(type(query2))
print(len(query2))
pretty_print(query2)
"""
query2 = queryByName(ARTIST_URL, query_type['simple'], "Queen")
queen = query2['artists']


print(len(queen))
print(queen)

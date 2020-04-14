import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

"""
This file is in charge of doing an initial data audit of the data types in the file.
returns a dictionary like:


"""

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "Cove", "Alley", "Park", "Way", "Walk" "Circle", "Highway",
            "Plaza", "Path", "Center", "Mission"]

mapping = {"Ave": "Avenue",
           "Ave.": "Avenue",
           "avenue": "Avenue",
           "ave": "Avenue",
           "Blvd": "Boulevard",
           "Blvd.": "Boulevard",
           "Blvd,": "Boulevard",
           "Boulavard": "Boulevard",
           "Boulvard": "Boulevard",
           "Ct": "Court",
           "Dr": "Drive",
           "Dr.": "Drive",
           "E": "East",
           "Hwy": "Highway",
           "Ln": "Lane",
           "Ln.": "Lane",
           "Pl": "Place",
           "Rd": "Road",
           "Rd.": "Road",
           "St": "Street",
           "St.": "Street",
           "st": "Street",
           "street": "Street",
            "E" : "East",
            "W" : "West",
            "S" : "South",
            "N" : "North"
           }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = collections.defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(street_name, mapping):
    street_name = street_name.replace(' ', ' ')
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        street_type2 = ' '.join(street_name.split()[0:])
        if street_type in mapping.keys():
            street_name = re.sub(street_type, mapping[street_type],street_name)
    return street_name


def update_postal_code(postal_code):
    postal_code = postal_code.upper()
    if ' ' not in postal_code:
        if len(postal_code) != 5:
            postal_code = postal_code[0:5]
    return postal_code

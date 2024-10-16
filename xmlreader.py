import xml.etree.ElementTree as ET

import xmltodict

from pprint import pprint

with open('alan.osrl') as fd:
    doc = xmltodict.parse(fd.read())

pprint(doc)

# tree = ET.parse('alan.osrl')
# root = tree.getroot()  
# print(root[1])

# # print the attributes of the first tag  
# print(root[0].attrib) 
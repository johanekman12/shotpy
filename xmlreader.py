import xmltodict

with open('alan.osrl') as fd:
    doc = xmltodict.parse(fd.read())

print(doc)
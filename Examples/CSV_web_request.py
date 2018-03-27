#!/usr/bin/env python3

import requests
# the regular expressions library
import re

# location of the document to get
url = "http://data.gov.uk/data/resource/nhschoices/Hospital.csv"
result = requests.get(url)

# break the result in to lines (\r\n indicates the end of a line)
processed = result.text.split('\r\n')
# split each line at the tab character (\t)
processed[:] = [ j.split('\t') for j in processed ]

print("Enter the start of a postcode: ", end="")
postcode = input()
print("")

# complie a regular expression
r = re.compile("^" + postcode, re.IGNORECASE)

for i in processed:
    print(i)

# go through each line in the data
for line in processed:
    # if the pattern matches, print the hospital and postcode, then a newline
    if r.match(line[13]):
        print(line[7])
        print(line[13])
        print("")


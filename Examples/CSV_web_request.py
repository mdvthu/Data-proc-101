#!/usr/bin/env python3

import requests
# the regular expressions library
import re

# location of the document to get
url = "http://data.gov.uk/data/resource/nhschoices/Hospital.csv"
result = requests.get(url)

# break the result in to lines (\r\n indicates the end of a line in our CSV file)
processed = result.text.split('\r\n')
# split each line at the tab character (\t)
processed[:] = [ j.split('\t') for j in processed ]
# Remove any empty lines
processed[:] = [ x for x in processed if len(x) > 1 ]

# Collect some user input and print a new line
# before outputting the results
print("Enter the start of a postcode: ", end="")
postcode = input()
print("")

# build a regular expression
# to allow searching by postcode
# the carat symbol (^) means match the start of a line
#
# regular expressions (regex) are an extremely powerful tool
# this only touches the very surface of what is possible
r = re.compile("^" + postcode, re.IGNORECASE)

# iterate through each line in the data
for line in processed:
    # if the pattern matches, print the hospital and postcode, then a newline
    if r.match(line[13]):
        print(line[7])
        print(line[13])
        print("")


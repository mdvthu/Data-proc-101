#!/usr/bin/env python3

import requests

url = "http://data.gov.uk/data/resource/nhschoices/Hospital.csv"
result = requests.get(url)

processed = result.text.split('\r\n')
processed[:] = [ j.split('\t') for j in processed ]

print(processed[0])

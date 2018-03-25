#!/usr/bin/env python3

# Requests is an elegant and simple HTTP library for Python
# It will allow you to contact a webserver to ask for information -- e.g. a webpage
# More info is available at: http://docs.python-requests.org/en/master/
import requests

# The name of the file to download. This can be any type of file
url = "https://mdvthu.com/files/example_text_file.txt"

# Go off to the internet and download the specified file
print("Downloading " + url + " from the internet...")
download = requests.get(url)

# Print the contents of the file
print("The contents of the file are:\n")
print(download.text)


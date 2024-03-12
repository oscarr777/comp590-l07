#!/usr/bin/python3

import requests
import json
import os

# setup some information
secret_key = '01qFegZQA8YAOn38ViC5S4Leld2sL3i1ueQhLWA0' # put your key in here
nasa_url = 'https://api.nasa.gov/planetary/apod?api_key=' + secret_key

# make the GET request
r = requests.get(nasa_url)

# did we get back some JSON?
print("Got a response from NASA!")
print(r.text)
print()

# load the data as json data
data = json.loads(r.text)
print("Found image url: " + data['url'])

# download the image into the downloads folder
print("Downloading...")
os.system("wget -P ../build/img " + data['url'])

# extract the filename, might be useful later
print("Downloaded file: " + data['url'].split('/')[-1])

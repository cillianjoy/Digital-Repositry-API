# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:10:41 2017

@author: Cillian Joy
Python script to call NUI Galway Library Digital Respositry API and save results to csv

"""

import requests
from pandas.io.json import json_normalize
import pandas as pd

import json

# API call, change to suit.
# The API returns 200 at a time, to get the next 200 use start. For example &start=200
url = 'https://digital.library.nuigalway.ie/islandora/rest/v1/solr/dc.relation:robinson*?fl=PID,dc.title,dc.description,mods_subject_topic_ms'
response = requests.get(url)
data = response.json()

print("Total datset has " + str(data['response']['numFound']) + " records. This query returned " + str(data['responseHeader']['params']['rows']) + " rows, starting at row " + str(data['response']['start']) + ".")

# Data to Pandas dataframe
df = json_normalize(data['response']['docs'])

test_item_id = df.iloc[0]['PID']

# Dump the first object to a json files
print "Outputting first object as a JSON file (in ./output)"
item_url = 'https://digital.library.nuigalway.ie/islandora/rest/v1/object/' + test_item_id
r = requests.get(item_url)
data = r.json()
with open('output/' + test_item_id.replace(':', '_') + '.json' , 'w') as outfile:
    json.dump(data, outfile, indent = 4)


print "Outputting first object JPG file, if it exists (in ./output)"
item_url = 'https://digital.library.nuigalway.ie/islandora/rest/v1/object/' + test_item_id + '/datastream/JPG'
r = requests.get(item_url)
if r.status_code == 200:
    with open('output/' + test_item_id.replace(':', '_') + '.jpg', 'wb') as f:
        f.write(r.content)



# Dump all objects to json files
# print "Dumping all objects as JSON files (in ./output)"
# for index, item in df.iterrows():
#     item_url = 'https://digital.library.nuigalway.ie/islandora/rest/v1/object/' + item['PID']
#     r = requests.get(item_url)
#     data = r.json()
#     with open('output/' + item['PID'].replace(':', '_') + '.json' , 'w') as outfile:
#         json.dump(data, outfile)


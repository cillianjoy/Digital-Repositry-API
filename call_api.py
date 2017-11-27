# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:10:41 2017

@author: Cillian Joy
Python script to call NUI Galway Library Digital Respositry API and save results to csv

"""

import requests
from pandas.io.json import json_normalize
import pandas as pd

#import json

# API call, change to suit
url = 'https://digital.library.nuigalway.ie/islandora/rest/v1/solr/dc.relation:robinson*?fl=PID,dc.title,dc.description,mods_subject_topic_ms'
response = requests.get(url)
data = response.json()

# Data to Pandas dataframe
df = json_normalize(data['response']['docs'])

# Print to screen and save to csv
print(df)
df.to_csv('data.csv')

#!/usr/local/bin/env python

import requests
import json
import csv
import os

samanage_username = str(os.getenv('SAMANAGE_USERNAME'))
samanage_key = str(os.getenv('SAMANAGE_KEY'))

if  samanage_username == None or samanage_key == None:
    print "Please setup SAMANAGE_KEY and SAMANAGE_USERNAME variables in your environement"
    quit()

url = 'https://apieu.samanage.com'
request = '/incidents.xml'

connect = requests.get(url+request, auth = (samanage_username, samanage_key))
print connect.text

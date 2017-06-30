#!/usr/local/bin/env python

import requests
import json
import csv
import os

#Call Samanage credentials from the environment
"""
samanage_username = str(os.getenv('SAMANAGE_USERNAME'))
samanage_key = str(os.getenv('SAMANAGE_KEY'))
"""
if  samanage_username == None or samanage_key == None:
    print "Please setup SAMANAGE_KEY and SAMANAGE_USERNAME variables in your environement"
    quit()

url = 'https://apieu.samanage.com'

request = requests.get(url, auth = (samanage_username, samanage_key))
print request.status_code

print "Enter your file path below"
filepath = raw_input()

with open(file, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    rownumber = 2

    for row in reader:
        if row[11] == 'P' or 'p':
            pass

        else if row[11] == 'M' or 'm':
            extension = '/other_assets/%s.xml' %(row[10])
            for entry in row:
                if entry[0] == '@':
                    content == entry[1:]
                    if row.index(entry) == 6:
                        field == 'Site'
                    else if row.index(entry) == 7:
                        field == 'Room'
                    else if row.index(entry) == 8:
                        field == 'Department'
                    else if row.index(entry) == 9:
                        field == 'User'
                    else:
                        continue
                    data = {"other_asset":{ "%s":"%s" }, } %(field, content)
                    data = json.dumps(data)
                    #request = requests.post(url+extension, auth=(samanage_username, samanage_key), data=json.dumps(data))

        else if row[11] == 'N' or 'n':
            extension = '/other_assets.xml'
            pass
        else:
            print "Error: Incomplete inventory status column, row %d. Row skipped." %(rownumber)
            next


        rownumber += 1

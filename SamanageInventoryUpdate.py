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

#test connection to the server
test = requests.get(url, auth = (samanage_username, samanage_key))
if test.status_code != 200:
    print "Error: Cannot connect to server."
    quit()
print test.status_code

#have user input their csv file
print "Enter your csv file path below"
filepath = raw_input()

#read file and update Samanage accordingly
with open(file, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    rownumber = 2

    for row in reader:
        if row[11] == 'P' or 'p':
            pass

        #for modified assets
        else if row[11] == 'M' or 'm':
            extension = '/other_assets/%s.xml' %(row[10])
            for entry in row:
                if entry[0] == '&':
                    content == entry[1:]
                    if row.index(entry) == 0:
                        field == 'name'
                    else if row.index(entry) == 1:
                        field == 'status'
                    else if row.index(entry) == 6:
                        field == 'site'
                    else if row.index(entry) == 7:
                        field == 'Room'
                    else if row.index(entry) == 8:
                        field == 'department'
                    else if row.index(entry) == 9:
                        field == 'User'
                    else:
                        continue
                    data = {"other_asset":{ "%s":"%s" }, } %(field, content)
                    data = json.dumps(data)
                    #request = requests.post(url+extension, auth=(samanage_username, samanage_key), data=data)

        #for new assets
        else if row[11] == 'N' or 'n':
            extension = '/other_assets.xml'
            data = {"other_asset": {"name": "%s", "asset_id": "%s",
            "asset_type": {"name": "%s"}, "status": {"name": "Operational"},
            "manufacturer": "%s", "model": "%s", "serial_number": "%s", "site": {"name": "%s"},
            "department": {"name": "%s"},  "custom_fields_values": {"custom_fields_value":[
            {"name": "Room", "value": "%s"}, {"name": "User", "value": "%s"} ] } } }
            %(row[0], row[10], row[2], row[1], row[3], row[4], row[5], row[6], row[8], row[7], row[9])
            data = json.dumps(data)
            #request = requests.post(url+extension, auth=(samanage_username, samanage_key), data=data)

        else:
            print "Error: Incomplete inventory status column, row %d. Row skipped." %(rownumber)
            next


        rownumber += 1

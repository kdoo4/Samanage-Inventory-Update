#!/usr/local/bin/env python

import requests
import json
import csv
import os

#Call Samanage credentials from the environment

samanage_username = str(os.getenv('SAMANAGE_USERNAME'))
samanage_key = str(os.getenv('SAMANAGE_KEY'))

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
filepath = raw_input().rstrip()

#read file and update Samanage accordingly
with open(filepath, 'rU') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    rownumber = 2

    for row in reader:
        if row[11].lower() == 'p':
            pass

        #for modified assets
        elif row[11].lower() == 'm':
            extension = '/other_assets/%s.json' %(row[10])
            for entry in row:
                if entry[0] == '&':
                    content == entry[1:]
                    if row.index(entry) == 0:
                        field == 'name'
                    elif row.index(entry) == 1:
                        field == 'status'
                    elif row.index(entry) == 6:
                        field == 'site'
                    elif row.index(entry) == 7:
                        field == 'room'
                    elif row.index(entry) == 8:
                        field == 'department'
                    elif row.index(entry) == 9:
                        field == 'user'
                    else:
                        continue
                    #Data input for the different fields
                    if field == 'name' or field == 'room':
                        data = {"other_asset":{ "%s":"%s" }, } %(field, content)
                    else:
                        data = {"other_asset":{"%s": {"name": "%s"}}} %(field, content)
                    data = json.dumps(data)
                    request = requests.post(url+extension, auth=(samanage_username, samanage_key), data=data)
                    print request.content

        #for new assets
        elif row[11].lower() == 'n':
            blanks = 0;
            for entry in row:
                if entry == '':
                    blanks += 1
            if blanks == 12:
                continue

            extension = '/other_assets.json'
            data = {"other_asset": {"name": row[0], "asset_id": row[10],
            "asset_type": {"name": row[2]}, "status": {"name": row[1]},
            "manufacturer": row[3], "model": row[4], "serial_number": row[5], "site": {"name": row[6]},
            "department": {"name": row[8]},  "custom_fields_values": {"custom_fields_value":[
            {"name": "room", "value": row[7]}, {"name": "user", "value": {"email": row[9]}} ] } } }
            data = json.dumps(data)
            print url+extension
            request = requests.post(url+extension, auth = (samanage_username, samanage_key), data=data)
            print request.content

        else:
            print "Error: Incomplete inventory status column, row %d. Row skipped." %(rownumber)



        rownumber += 1

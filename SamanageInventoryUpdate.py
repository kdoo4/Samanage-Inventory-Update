#!/usr/local/bin/env python

import requests
import json
import csv
import os

#Call Samanage credentials from the environment

samanage_token = str(os.getenv('SAMANAGE_TOKEN'))

if  samanage_token == None:
    print "Please setup SAMANAGE_TOKEN variable in your environement"
    quit()

headers = {
    'X-Samanage-Authorization': 'Bearer %s' %(samanage_token),
    'Accept': 'application/vnd.samanage.v2.1+json',
    'Content-Type': 'application/json',
}
url = 'https://apieu.samanage.com'

#Test request to server
request = requests.get("", headers=headers)
print request.status_code


#have user input their csv file
print "Enter your csv file path below"
filepath = raw_input().rstrip()

#read file and update Samanage accordingly
with open(filepath, 'rU') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    rownumber = 2

    for row in reader:
        if row[12].lower() == 'p':
            pass

        """For Modified Assets: Checks the fields that would have been Modified
        and updates them in Samanage """
        elif row[12].lower() == 'm':
            extension = '/other_assets/%d.json' %(row[0])
            for entry in row:
                #Preceding character to signify updated field
                if entry[0] == '&':
                    content = str(entry[1:])
                    if row.index(entry) == 1:
                        field = 'name'
                    elif row.index(entry) == 2:
                        field = 'status'
                    elif row.index(entry) == 7:
                        field = 'site'
                    elif row.index(entry) == 8:
                        field = 'room'
                    elif row.index(entry) == 9:
                        field = 'department'
                    elif row.index(entry) == 10:
                        field = 'user'
                    else:
                        continue
                    #Samanage data formats for the different fields
                    if field == 'name' or field == 'room':
                        data = {"other_asset":{field: content}, }
                    else:
                        data = {"other_asset":{field: {"name": content}}}
                    data = json.dumps(data)
                    print url+extension
                    request = requests.post(url+extension, headers=headers, data=data)
                    print request.status_code
                    print request.content

        #Creating new assets
        elif row[12].lower() == 'n':
            #Check to make sure no blank rows are made as assets
            blanks = 0;
            for entry in row:
                if entry == '' of ' ':
                    blanks += 1
            if blanks == 13:
                continue

            #Grab data from row and put it into json format
            extension = '/other_assets.json'
            data = {"other_asset": {"name": row[1], "asset_id": row[11],
            "asset_type": {"name": row[3]}, "status": {"name": row[2]},
            "manufacturer": row[4], "model": row[5], "serial_number": row[6], "site": {"name": row[7]},
            "department": {"name": row[9]},  "custom_fields_values": {"custom_fields_value":[
            {"name": "room", "value": row[8]}, {"name": "user", "value": {"email": row[10]}} ] } } }
            data = json.dumps(data)
            print url+extension
            request = requests.post(url+extension, headers=headers, data=data)
            print request.status_code

        #Check for unaccounted for assets
        else:
            print "Error: Incomplete inventory status column, row %d. Row skipped." %(rownumber)



        rownumber += 1

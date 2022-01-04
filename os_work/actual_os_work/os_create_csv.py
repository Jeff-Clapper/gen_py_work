"""Practice with OS ans CSV file creation, with the extended purpose of analyzing categories that Plaid provides for transactions"""

import os
import csv 
import requests
import json

url = "https://sandbox.plaid.com/categories/get"
payload = json.dumps({})
headers = {
    'Content-Type': 'application/json'
}
response = requests.request("POST",url,headers=headers,data=payload)
data1 = response.json()



categories = data1['categories']
here = os.getcwd()
target = # PATH HERE
file = "plaid_categories.csv"

complete_path = os.path.join(target,file)

with open(complete_path,'w', newline='') as myFile:
    writer = csv.writer(myFile)
    writer.writerow(['cat_id','group','major_cat','minor_cat_1','minor_cat_2','minor_cat_3'])
    rows = []
    for category in categories:
        row = [category['category_id'],category['group']]
        for cat in category['hierarchy']:
            row.append(cat)
        rows.append(row)

    writer.writerows(rows)

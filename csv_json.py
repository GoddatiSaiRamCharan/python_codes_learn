import json
csv_open=open("csv_file.txt","r")
csv_content=[line.strip() for line in csv_open.readlines()]
csv_open.close()
new_csvcontent=[]
for content in csv_content:
    content=content.split(",")
    club=content[0]
    country=content[2]
    city=content[1]
    ndata={"club" : club , "country":country , "city":city }
    new_csvcontent.append(ndata)
print(new_csvcontent)
json_write=open("json_file.txt","w")
json.dump(new_csvcontent,json_write)
json_write.close()

import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

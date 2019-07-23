import json

with open('blocketData.json') as json_data:
  jsonData = json.load(json_data)

for i in jsonData:
  if "bmw" in i["title"].lower():
    print(i)

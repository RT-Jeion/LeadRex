import json


with open("leads.json", "r", encoding="utf-8") as f:
    data = json.load(f)


for link in data:
    name = link["URL"].split(".com")[0].split("://")[-1].strip("www.").strip("/")
    print(name)

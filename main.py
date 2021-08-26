#!/usr/bin/python
import jinja2
import json
import requests

#to get data
res = requests.get('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
data=json.loads(res.text)
data_serialized= json.dump(data, open('data.json', "w"),indent=2)

#to write data and display 
templateFilePath = jinja2.FileSystemLoader('./')
jinjaEnv = jinja2.Environment(loader=templateFilePath)
jTemplate = jinjaEnv.get_template("html-template.html") #html template
with open("data.json") as config:
    config = json.load(config)
    output = jTemplate.render(config)
    print(output)
    outFileH = open('index.html', 'w') #html output
    outFileH.write(output)
    outFileH.close()
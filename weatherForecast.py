### Simple program to take Weather JSON data and return as string

import urllib.request
import json
from setup import obsUrl

urllib.request.urlretrieve(obsUrl, 'weatherForecast.json')

with open('weatherForecast.json') as json_file:
    data = json.load(json_file)

dictLen = len(data['time']) - 1
n = 0
for w in data:
    dayString = data['time']['startPeriodName'][n]
    tempLabel = data['time']['tempLabel'][n]
    tempString = str(data['data']['temperature'][n])
    textString = data['data']['text'][n]
    weatherString = dayString + " " + tempLabel + " " + tempString + " " + textString + "\n"
    n = n + 1


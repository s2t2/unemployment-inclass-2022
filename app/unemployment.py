
# this is the "app/unemployment_report.py" file...
import os
import json
from pprint import pprint
import statistics

import requests
from dotenv import load_dotenv

load_dotenv()
#API_KEY="demo"
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
#print(type(parsed_response))
#pprint(parsed_response)

# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.


#print(parsed_response.keys())
data = parsed_response["data"]
print(type(data))
#print(parsed_response)
print(data[0])
print()
print("CURRENT UNEMPLOYMENT RATE:")
print(data[0]["value"]+ "%")

# Challenge B
# 
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

unemploymentData = json.loads(response.text)
#pprint(unemploymentData)
#print(type(unemploymentData))
print()
dates = []
values = []
for day in unemploymentData['data']:
    dates.append(day['date'])
    values.append(float(day['value']))
    
print("AVERAGE UNEMPLOYMENT RATE:", statistics.mean(values))
print("Number of months:",len(dates))
print()



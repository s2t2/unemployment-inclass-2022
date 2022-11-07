
# this is the "app/unemployment_report.py" file...
import json
from pprint import pprint
import statistics

import requests
import plotly.express as px
from app.alpha import API_KEY


request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)


# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.

data = parsed_response["data"]
print()
print("CURRENT UNEMPLOYMENT RATE:")
print(data[0]["value"]+ "%")

# Challenge B
# 
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

unemploymentData = json.loads(response.text)

print()
dates = []
values = []
for day in unemploymentData['data']:
    dates.append(day['date'])
    values.append(float(day['value']))
    
print("AVERAGE UNEMPLOYMENT RATE:", round(statistics.mean(values),2))
print("Number of months:",len(dates))
print()

# Challenge C
# 
# Plot a line chart of unemployment rates over time.
print("LOADING CHART OF UNEMPLOYMENT OVER TIME...")
print()
fig = px.line(x=dates, y=values)
fig.update_layout(title="Unemployment Over Time",yaxis_title=f"Unemployment",xaxis_title="Date",yaxis_ticksuffix='%')
fig.show()

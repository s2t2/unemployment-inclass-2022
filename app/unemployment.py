
# this is the "app/unemployment_report.py" file...
import json
from pprint import pprint
import statistics

import requests
import plotly.express as px
from app.alpha import API_KEY

def format_pct(my_number):
    """
    Formats a percentage number like 3.6555554 as percent, rounded to two decimal places.
    Param my_number (float) like 3.6555554
    Returns (str) like '3.66%'
    """
    return f"{my_number:.2f}%"



def fetch_unemployment_data():
    """Fetches unemployment data from the AlphaVantage API. Returns a list of dictionaries."""
    request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)
    #print(type(parsed_response))
    #pprint(parsed_response)

    # TODO: consider converting string rates to floats before returning the data
    # TODO: consider creating and returning a pandas DataFrame, if you like that kind of thing
    return parsed_response["data"]



# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.

data = fetch_unemployment_data()
print()
print("CURRENT UNEMPLOYMENT RATE:")
print(data[0]["value"]+ "%", "as of", data[0]["date"])

# Challenge B
# 
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

 
print()

this_year = [d for d in data if "2022-" in d["date"]]
currentRates = [float(d["value"]) for d in this_year]
    
print("AVERAGE UNEMPLOYMENT THIS YEAR:", format_pct(statistics.mean(currentRates)))
print("Number of months:",len(this_year))
print()

# Challenge C
# 
# Plot a line chart of unemployment rates over time.

dates = [d["date"] for d in data]
values = [float(d["value"]) for d in data]
print("LOADING CHART OF UNEMPLOYMENT OVER TIME...")
print()
fig = px.line(x=dates, y=values)
fig.update_layout(title="Unemployment Over Time",yaxis_title=f"Unemployment",xaxis_title="Date",yaxis_ticksuffix='%')
fig.show()

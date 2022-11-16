import json
from pprint import pprint
from statistics import mean

import requests
from plotly.express import line

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

from app.unemployment import format_pct, fetch_unemployment_data


def test_percent_sign_formatting():

    assert format_pct(3.65554) == '3.66%'

    assert format_pct(25.4) == '25.40%'


def test_fetch_data():
    # this function will return a list of datapoints
    data = fetch_unemployment_data()
    assert isinstance(data, list)

    # how did our program need to be referencing this data?
    # Challenge A seems to take the first item and print its value and date keys
    # the latest values and dates will change, so we can't test the exact values in this case
    # but we can at least test the structure:
    latest = data[0]
    assert isinstance(latest, dict)
    assert "date" in latest.keys()
    assert "value" in latest.keys()
    assert isinstance(latest["date"], str)
    assert isinstance(latest["value"], str) # NOTE: the rates are strings!!!

    # in this case, we do know what the earliest value is, so
    # we can test it for good measure, to give us a sense of the structure of each item in the list
    earliest = data[-1]
    assert earliest == {'date': '1948-01-01', 'value': '3.4'}

    # testing the second to last value could give us some clue about the frequency
    # here it looks like we are expecting monthly frequency
    assert data[-2] == {'date': '1948-02-01', 'value': '3.8'}
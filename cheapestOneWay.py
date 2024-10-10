import csv
import requests
import json
from searchCriteria import DEPARTURE_AIRPORT,ARRIVAL_AIRPORT,DEPARTURE_DATE,CURRENCY,CABIN_CLASS,ADULTS 
import os as os

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    try:
        from config import API_KEY
    except ImportError:
        raise RuntimeError("API_KEY not found in environment variables or config.py")

def writeToJSON(data): 
    with open('results/cheapestOneWay.json', 'w') as f:
        json.dump(data, f, indent=4)
        print("Prices have been saved to prices.json file.")

def writeToCSV(airport, data): 
    with open(f'results/{airport}.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['day', 'group', 'price'])
        writer.writeheader()
        for item in data["data"]:
            writer.writerow(item)

def makeAPICall(): 
    
    Arrival_Airports = ["AMS"] 
    
    for airport in Arrival_Airports:
        url = "https://sky-scanner3.p.rapidapi.com/flights/cheapest-one-way"
        querystring = {"fromEntityId":DEPARTURE_AIRPORT,"toEntityId":airport,"departDate":DEPARTURE_DATE, "currency":CURRENCY, "cabinClass":CABIN_CLASS, "adults":ADULTS}
        headers = {
	        "X-RapidAPI-Key": API_KEY,
	        "X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
        }
        
    try: 
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        
        writeToCSV(airport, data)
    
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
makeAPICall()



import csv
import requests
import json
from searchCriteria import DEPARTURE_AIRPORT,ARRIVAL_AIRPORT,DEPARTURE_DATE,CURRENCY,CABIN_CLASS,ADULTS 
import os as os

#API_KEY = os.getenv('API_KEY')
API_KEY = "090838f38cmsh0b14c91638b52a6p146c9bjsn2e69a62822bc"
if not API_KEY:
    try:
        from config import API_KEY
    except ImportError:
        raise RuntimeError("API_KEY not found in environment variables or config.py")

def write_to_json(data): 
    """_summary_

    Args:
        data (_type_): _description_
    """
    with open('results/departures/cheapestOneWay.json', 'w') as f:
        json.dump(data, f, indent=4)
        print("Prices have been saved to prices.json file.")

def write_to_csv(data):
    """_summary_

    Args:
        data (_type_): _description_
    """
    with open(f'results/departures/departure.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['day', 'group', 'price'])
        writer.writeheader()
        for item in data["data"]:
            writer.writerow(item)

def make_api_request(): 
    """_summary_

    Args:
        data (_type_): _description_
    """
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
        
        return data
        
    
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")

def main(): 
    """_summary_

    Args:
        data (_type_): _description_
    """
    data = make_api_request()
    write_to_csv(data)
                            
main()
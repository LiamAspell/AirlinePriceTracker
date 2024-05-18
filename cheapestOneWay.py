import requests
import json
from config import API_KEY
from searchCriteria import DEPARTURE_AIRPORT,ARRIVAL_AIRPORT,DEPARTURE_DATE,CURRENCY,CABIN_CLASS,ADULTS 

url = "https://sky-scanner3.p.rapidapi.com/flights/cheapest-one-way"

querystring = {"fromEntityId":DEPARTURE_AIRPORT,"toEntityId":ARRIVAL_AIRPORT,"departDate":DEPARTURE_DATE, "currency":CURRENCY, "cabinClass":CABIN_CLASS, "adults":ADULTS}

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)



data = response.json()


# Write the data to a JSON file
with open('cheapestOneWay.json', 'w') as f:
    json.dump(data, f, indent=4)
    print("Prices have been saved to prices.json file.")
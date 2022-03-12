import requests
import pandas as pd
import random
from date_manager import DateManager

HEADERS = {"apikey": "9ALMvuZsoHoMKdiCAyOD2p6186wSw1-k"}
tequila_endpoint = "http://tequila-api.kiwi.com/"
query_endpoint = "locations/query"
search_endpoint = "v2/search"
check_flights = "/booking/check_flights"


class FlightData:
    def __init__(self, file_name):
        self.destinations = []
        self.place = []
        self.details_df = pd.read_csv(file_name)
        self.pod_json = {"term": {(self.details_df["details"].values[1])}}
        # takes array from df and fixes it
        self.details_df = pd.read_csv(file_name)
        self.destinations2 = (self.details_df["details"].values[3])
        self.place = random.choice(self.destinations2.split())
        self.place = self.place.replace("(", "").replace(")", "").replace(",", "").replace("'", "")
        self.poa_json = {"term": self.place}

        # calculate dates for tequila
        self.DM1 = DateManager(months_ahead=2)
        self.DM2 = DateManager(months_ahead=4)
        self.DATE_FROM = (self.DM1.date_calculator())
        self.DATE_TO = (self.DM2.date_calculator())

    def find_pod(self):
        # finds departing airport code for API
        self.response = requests.get(url=(tequila_endpoint + query_endpoint), params=self.pod_json, headers=HEADERS)
        self.data = self.response.json()
        self.pod_code = self.data["locations"][0]["id"]

    def find_poa(self):
        # finds arriving airport code for API
        self.response1 = requests.get(url=(tequila_endpoint + query_endpoint), params=self.poa_json, headers=HEADERS)
        try:
            self.data1 = self.response1.json()
        except KeyError:
            print("Something went wrong, trying again")
            self.find_poa()
        self.poa_code = self.data1["locations"][0]["id"]

    def flight_search(self):
        self.travel_json = {"fly_from": f"{self.pod_code}",
                            "fly_to": f"{self.poa_code}",
                            "date_from": f"{self.DATE_FROM}",
                            "date_to": f"{self.DATE_TO}",
                            "currency": f"{self.details_df['details'].values[4]}"
                            }

        response = requests.get(url=(tequila_endpoint + search_endpoint), params=self.travel_json, headers=HEADERS)
        return response.json()



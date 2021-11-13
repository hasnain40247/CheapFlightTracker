from pprint import pprint

import requests

from endpoints import *


class Flight:
    def getCityCode(self,city_name):

        query = {"term": city_name, "location_types": "city"}

        response = requests.get(url=location_endpoint, headers=kiwi_headers, params=query)
        results = response.json()["locations"]
        return results[0]["code"]

    def getSearches(self,fly_to,date_from,date_to):
        parameters = {
            "fly_from": "LON",
            "fly_to":  fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        kiwi_response = requests.get(url=kiwi_endpoint, params=parameters, headers=kiwi_headers)
        pprint(kiwi_response.json())
        return kiwi_response
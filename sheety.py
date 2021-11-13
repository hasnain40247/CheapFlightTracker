import requests

from endpoints import sheety_endpoint
from flight import Flight


class Sheety:

    def getSheetData(self):

        sheety_response = requests.get(url=sheety_endpoint)
        return sheety_response.json()["prices"]

    def updateIndex(self, getDestinationData):
        responses = []

        for object in getDestinationData:

            if object["iataCode"] == "":
                endpoint = f"{sheety_endpoint}/{object['id']}"
                json = {
                    "price": {
                        "iataCode": Flight().getCityCode(object["city"])
                    }
                }
                sheety_response = requests.put(url=endpoint, json=json)
                responses.append(sheety_response.text)
        return responses

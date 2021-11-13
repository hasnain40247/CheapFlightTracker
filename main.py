import datetime

from endpoints import account_sid, auth_token
from flight import Flight
from pprint import pprint
from twilio.rest import Client
from flightData import FlightData
from sheety import Sheety

response = Sheety().updateIndex(Sheety().getSheetData())

tmr_date = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
sixmnt_date = (datetime.datetime.today() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")

getDestinationData = Sheety().getSheetData()
dataList = []
print(getDestinationData)
for item in getDestinationData:
    kiwi_response = Flight().getSearches(item["iataCode"], tmr_date, sixmnt_date)
    try:
        data = kiwi_response.json()["data"][0]
        low = data["price"]
        print(data["route"][0]["local_departure"].split("T")[0])
        print(  data["route"][1]["local_departure"].split("T")[0])
        flightDataObject = FlightData(
            data["route"][0]["local_departure"].split("T")[0],
            data["route"][1]["local_departure"].split("T")[0],
            data["flyFrom"], data["flyTo"], data["route"][0]["cityFrom"], data["route"][0]["cityTo"],
            item["lowestPrice"], low)
        print(type(low))
        print(type(item["lowestPrice"]))
        dataList.append(flightDataObject)
    except:
        print("Not Found")

for item in dataList:
    print(f"{item.oprice} < {item.sprice}")
    if item.oprice < item.sprice:
        client = Client(account_sid, auth_token)

        msg=f"Low Price Alert!\n Only ₹{item.oprice} to fly from {item.originCity}-{item.originAir} to {item.destCity}-{item.destAir}, from {item.fromDate} to {item.toDate}"
        print(item.fromDate)
        message = client.messages.create(
            body=msg,
            from_='whatsapp:+14155238886',
            to='whatsapp:xxxxxxxxx'
        )
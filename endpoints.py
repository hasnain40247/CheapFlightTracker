import os

sheety_endpoint = "https://api.sheety.co/c3f4584fadfa17ed350cc92f8a9c962f/flightDeals/prices"
location_endpoint = f"https://tequila-api.kiwi.com/locations/query"
kiwi_headers = {
    "apikey": os.environ["apikey"]
}
kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
account_sid = "AC40115e87d53567139128a718375635c2"
auth_token = os.environ["auth_token"]

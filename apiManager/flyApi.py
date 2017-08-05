
import requests
import json
import pprint
from apiManager import apiKeys as k

class apiManager():
    def __init__(self):

        "Initialize the Api link"

        self.url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key="


    def search(self):

        url = self.url
        url += k.apex_ApiKey

        headers = {'Content-Type': 'application/json'}

        body = {
            "request": {
                "passengers": {
                    "adultCount": 1},
                "slice":[{
                    "origin": "MSP",
                    "destination": "ABJ",
                    "date": "2017-08-20"
                }]
            }
        }


        response  = requests.post(url, data=json.dumps(body), headers=headers)
        data = response.json()

        data_info = data['trips']['tripOption']


        prices = []

        for trips in data_info[0:10]:

            price = trips['pricing'][0]['baseFareTotal']
            prices.append(price)

        return prices


if __name__ == "__main__":

    "For Testing Porpose Only"

    apiObject = apiManager()
    prices = apiObject.search()
    print(prices)
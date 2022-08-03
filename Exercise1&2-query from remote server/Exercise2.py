import requests
import json

# https://www.w3schools.com/python/ref_requests_post.asp
# https://andmed.stat.ee/en/stat/majandus__energeetika__energia-tarbimine-ja-tootmine__luhiajastatistika/KE21/table/tableViewLayout2


def getQuery_paraSet(s, string_getValue):
    # defining a query params
    query = {'query': string_getValue}
    # sending get request and saving the response as response object
    r = requests.post(url=s.URL, data=query)
    #Checking the result
    jsonReturned = r.text
    # print(jsonReturned)
    y = json.loads(jsonReturned)
    # print(y)
    # print(y["results"]["bindings"][0]["sub"]["value"])
    # print(y["results"]["bindings"][0]["obj"]["value"])
    dicToReturn = {}
    for i in range(6):
        paraName = y["results"]["bindings"][i]["sub"]["value"].split("#")[1]
        paraValue = y["results"]["bindings"][i]["obj"]["value"]
        dicToReturn[paraName] = paraValue
    # print(listToReturn[0][1])
    return dicToReturn


if __name__ == '__main__':
    URL = "https://andmed.stat.ee/api/v1/en/stat/KE21"
    query = {
        "query": [{
            "code": "Aasta",
            "selection": {
                "filter": "item",
                "values": ["2022"]
            }
        }, {
            "code": "Kuu",
            "selection": {
                "filter": "item",
                "values": ["5"]
            }
        }, {
            "code": "Näitaja",
            "selection": {
                "filter": "item",
                "values": ["1", "3"]
            }
        }],
        "response": {
            "format": "json-stat2"
        }
    }

    r = requests.post(url=URL, json=query)  #json, not data !!
    #Checking the result
    jsonReturned = json.loads(r.text)
    electricity_total = jsonReturned["value"][0]
    electricity_wind = jsonReturned["value"][1]
    percentage = electricity_wind / electricity_total

    print(percentage)

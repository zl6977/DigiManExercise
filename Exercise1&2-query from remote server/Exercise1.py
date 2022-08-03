import requests 
import json
    
# https://www.w3schools.com/python/ref_requests_get.asp
# http://api.weatherapi.com/v1/current.json?key=f22e7e21dda14f8e8e8123743221406&q=Kohtla-Järve&aqi=no


def getQuery_paraSet(s, string_getValue):
    # defining a query params 
    query = {'query': string_getValue}
    # sending get request and saving the response as response object 
    r = requests.post(url = s.URL, data = query)
    #Checking the result
    jsonReturned = r.text
    # print(jsonReturned)
    y = json.loads(jsonReturned)
    # print(y)
    # print(y["results"]["bindings"][0]["sub"]["value"])
    # print(y["results"]["bindings"][0]["obj"]["value"])
    dicToReturn={}
    for i in range(6):
        paraName = y["results"]["bindings"][i]["sub"]["value"].split("#")[1]
        paraValue = y["results"]["bindings"][i]["obj"]["value"]
        dicToReturn[paraName] = paraValue
    # print(listToReturn[0][1])
    return dicToReturn

if __name__ == '__main__':
    URL = "http://api.weatherapi.com/v1/current.json?key=f22e7e21dda14f8e8e8123743221406&q=Kohtla-Järve&aqi=no"
    # query = {'query': string_getValue}
    # r = requests.post(url = URL, data = query)
    x = requests.get(URL)
    #Checking the result
    jsonReturned = json.loads(x.text)
    temperature = jsonReturned["current"]["temp_c"]
    print(temperature)

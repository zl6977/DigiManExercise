import requests
import json

# https://www.w3schools.com/python/ref_requests_post.asp
# https://andmed.stat.ee/en/stat/majandus__energeetika__energia-tarbimine-ja-tootmine__luhiajastatistika/KE21/table/tableViewLayout2

# def getQuery_paraSet(s, string_getValue):
#     # defining a query params
#     query = {'query': string_getValue}
#     # sending get request and saving the response as response object
#     r = requests.post(url=s.URL, data=query)
#     #Checking the result
#     jsonReturned = r.text
#     # print(jsonReturned)
#     y = json.loads(jsonReturned)
#     # print(y)
#     # print(y["results"]["bindings"][0]["sub"]["value"])
#     # print(y["results"]["bindings"][0]["obj"]["value"])
#     dicToReturn = {}
#     for i in range(6):
#         paraName = y["results"]["bindings"][i]["sub"]["value"].split("#")[1]
#         paraValue = y["results"]["bindings"][i]["obj"]["value"]
#         dicToReturn[paraName] = paraValue
#     # print(listToReturn[0][1])
#     return dicToReturn


def DoAction(URL, postBody, ready):
    if ready == True:
        r = requests.post(url=URL, json=postBody)  #json, not data !!
        #Checking the result
        jsonReturned = json.loads(r.text)
        print(jsonReturned)
        if jsonReturned["code"] == 202:
            isDone = True
        else:
            isDone = False
        return isDone
    else:
        return False


if __name__ == '__main__':
    readyFlag = True
    url = "http://escop.rd.tut.fi:3000/RTU/SimROB7/services/LoadPallet"
    postBody = {"destUrl": "http://escop.rd.tut.fi:3000/"}
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV7/services/TransZone35"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV8/services/TransZone14"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV8/services/TransZone45"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV9/services/TransZone14"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV9/services/TransZone45"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV10/services/TransZone14"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV10/services/TransZone45"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV11/services/TransZone14"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV11/services/TransZone45"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV12/services/TransZone14"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV12/services/TransZone45"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV1/services/TransZone12"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimCNV1/services/TransZone23"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimROB1/services/LoadPaper"
    readyFlag = DoAction(url, postBody, readyFlag)

    url = "http://escop.rd.tut.fi:3000/RTU/SimROB1/services/UnloadPaper"
    readyFlag = DoAction(url, postBody, readyFlag)
    
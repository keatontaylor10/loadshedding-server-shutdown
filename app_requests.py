import requests
import json

headers = {"Token":"C098C571-28344938-97AC0369-F03F1097"}


def getStageInfo():
    response = requests.get("https://developer.sepush.co.za/business/2.0/status", headers=headers)
    return response.json()

def areaSearch(area):
    response = requests.get("https://developer.sepush.co.za/business/2.0/areas_search?text=" + area, headers=headers)
    return response.json()


def areaInfo(area_code):
    response = requests.get("https://developer.sepush.co.za/business/2.0/area?id=" + area_code , headers=headers)
    return response.json()


print(areaInfo("westerncape-2-universityofstellenbosch")["events"])







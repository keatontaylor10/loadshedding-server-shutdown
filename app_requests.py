import requests
import config
headers = {"Token":config.ESP_token}


def getStageInfo():
    response = requests.get("https://developer.sepush.co.za/business/2.0/status", headers=headers)
    return response.json()

def areaSearch(area):
    response = requests.get("https://developer.sepush.co.za/business/2.0/areas_search?text=" + area, headers=headers)
    return response.json()


def areaInfo(area_code):
    response = requests.get("https://developer.sepush.co.za/business/2.0/area?id=" + area_code   , headers=headers)
    return response.json()


import requests
import json


def getHkHoliday():
    HOLIDAY_LIST = 'holidayList.json'

    holidayList = {}
    res = requests.get('http://www.1823.gov.hk/common/ical/en.json')

    reshoildayList = res.json()
    print("holiday data: ", reshoildayList)


getHkHoliday()

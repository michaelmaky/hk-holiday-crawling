import requests
import json
from datetime import datetime
from Models.Holiday import Holiday, HolidayEncoder


def getHkHolidayByYear(year=None):
    HOLIDAY_LIST = 'holidayList.json'

    holidayList = []
    res = requests.get('http://www.1823.gov.hk/common/ical/en.json')
    res.encoding = 'utf-8-sig'

    reshoildayList = res.json()['vcalendar'][0]['vevent']

    # if year not input, default is current year
    if year is None:
        currentYear = datetime.now().year
        year = str(currentYear)

    # filtered by specific year
    filteredHolidayList = [o for o in reshoildayList if o['dtstart']
                           [0].startswith(year)]

    # loop and push to model
    for holiday in filteredHolidayList:
        newHoliday = Holiday(
            holiday['uid'], holiday['dtstart'][0], holiday['summary'])
        holidayList.append(newHoliday)

    # print in json format
    print("holidayList: ", json.dumps(holidayList, indent=4, cls=HolidayEncoder))


getHkHolidayByYear()

#!/usr/bin/python3

import requests
import json
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim, GeoNames

def getuserinfo(user_public_id):
    # get user basic info (picture,username, timezone)

    response = requests.get("https://torre.bio/api/bios/{}"
                            .format(user_public_id))

    userpicture = response.json()['person'].get('picture')

    username = response.json()['person'].get('name')

    timezone = response.json()['person']['location'].get('timezone')

    return {"name": username,
            "photo": userpicture,
            "timezone": timezone
            }

def gettimezone(city):
    #get time zone from location lat and log

    num = Nominatim(user_agent='tz_filter')
    place, cord = (lat, lng) = num.geocode(city)
    geo = GeoNames(username='jdavp', user_agent='tz_filter')
    timezone = geo.reverse_timezone(cord)

    return timezone

def opportunitys():
    # get offer in the same time zone 

    response = requests.post("https://search.torre.co/opportunities/_search/?offset=0&size=10").json()
    df = pd.json_normalize(response["results"])
    columns = df[["id", 'objective', "locations", "remote"]]
    columns['aretherelocations'] =  columns["locations"].apply(lambda x: 1 if len(x) > 0 else 0)
    offers_remote_location = columns[(columns['remote'] & columns['aretherelocations'] == 1)]
    columns['timezone'] = columns.['locations'].apply(lambda x: gettimezone(x))
    
    print(offers_remote_location)
    return 0

opportunitys()
gettimezone('Brasil')
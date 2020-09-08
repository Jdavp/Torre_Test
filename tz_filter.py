#!/usr/bin/python3
import requests
import json
import numpy as np
import pandas as pd
import io

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


def opportunitys():
    # get offer in the same time zone 

    response = requests.post("https://search.torre.co/opportunities/_search/?offset=0&size=100")
    j = response.json()
    df = pd.json_normalize(j["results"])
    columns = df[["id", 'objective', "locations", "remote"]]
    columns['aretherelocations'] =  columns["locations"].apply(lambda x: 1 if len(x) > 0 else 0)
    offers_remote_location = columns[(columns['remote'] & columns['aretherelocations'] == 1)]
    
    print(y)
    return 0

opportunitys()
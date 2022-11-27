import os
import requests
import pandas as pd
import numpy as np

# storing our api key
api_key = os.environ.get('nsrdbKey')

def grab_nsrdb_data(year, email, lat, long, atts, interval, name, key):

    # params
    api_key=key
    year = str(year)  # '2019'
    email = str(email)  # 'aangelsalazarr@gmail.com'
    lat = str(lat)  # str(29.758938)
    lon = str(long)  # str(-95.367697)
    attributes = str(atts)  # 'ghi,dhi,dni,wind_speed,air_temperature,' \
    # 'solar_zenith_angle'
    leap_year = 'false'
    interval = str(interval)  # str(60)  # between 30, 60 mins
    utc = 'false'  # local timezone
    name = str(name)  # 'Angel+Salazar'  # use '+' instead of spaces
    mailing_list = 'false'  # true to be put on their mailing list
    affiliation = 'non'  # insert institution if you would like
    reason = 'ml+model+testing'  # insert your reason for use

    url = 'https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv?wkt=' \
          'POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&' \
          'utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&' \
          'mailing_list={mailing_list}&reason={reason}&api_key={api}&' \
          'attributes={attr}'.format(year=year,
                                     lat=lat,
                                     lon=lon,
                                     leap=leap_year,
                                     interval=interval,
                                     utc=utc,
                                     name=name,
                                     email=email,
                                     mailing_list=mailing_list,
                                     affiliation=affiliation,
                                     reason=reason,
                                     api=api_key,
                                     attr=attributes)

    # creating out df
    df = pd.read_csv(url, skiprows=2)

    return df

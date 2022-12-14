import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from datetime import date
from dateutil.relativedelta import relativedelta

# setting up params
rc('mathtext', default='regular')
plt.rcParams['figure.autolayout'] = True

# storing our api key in var api_key
api_key = os.environ.get('eiaAPI')


# purpose is to take out any rows where value is not a number/float
def is_float(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


# purpose is to grab data and transform it
def sun_energy_gen_data(state, start_date):
    '''

    :param state:
    :param start_date:
    :return:
    '''

    # base url
    baseUrl = 'https://api.eia.gov/v2/electricity/facility-fuel/data/'
    baseUrl = baseUrl + '?api_key=' + str(api_key)

    # we will want to add some inputs to our complete url
    urlData = '&data[0]=generation'
    urlFreq = '&frequency=monthly'
    urlStart = '&start=' + str(start_date)
    urlFacet = '&facets[fuel2002][0]=SUN&facets[state][0]=' + str(state)

    # concatenate to get main url
    url = baseUrl + urlData + urlFacet + urlFreq + urlStart

    r = requests.get(url=url)  # store url request as variable r
    data = r.json()  # convert our request into json format
    entries = data['response']['data']  # only grabbing data aspect of return
    df = pd.DataFrame(data=entries)  # converting our data into a pandas df
    df.reset_index(drop=True)  # resetting df index
    # df['period'] = pd.to_datetime(df['period'])  # convert period type

    return df  # return our now transformed df


def wind_energy_gen_data(state, start_date):
    '''

    :param state:
    :param start_date:
    :return:
    '''

    # base url
    baseUrl = 'https://api.eia.gov/v2/electricity/facility-fuel/data/'
    baseUrl = baseUrl + '?api_key=' + str(api_key)

    # we will want to add some inputs to our complete url
    urlData = '&data[0]=generation'
    urlFreq = '&frequency=monthly'
    urlStart = '&start=' + str(start_date)
    urlFacet = '&facets[fuel2002][0]=WND&facets[state][0]=' + str(state)

    # concatenate to get main url
    url = baseUrl + urlData + urlFacet + urlFreq + urlStart

    r = requests.get(url=url)  # store url request as variable r
    data = r.json()  # convert our request into json format
    entries = data['response']['data']  # only grabbing data aspect of return
    df = pd.DataFrame(data=entries)  # converting our data into a pandas df
    df.reset_index(drop=True)  # resetting df index
    # df['period'] = pd.to_datetime(df['period'])  # convert period type

    return df  # return our now transformed df


def hourly_energy_gen_data(start_time, fueltype, apikey):
    # base url
    baseUrl = 'https://api.eia.gov/v2/electricity/rto/fuel-type-data/data/'
    baseUrl = baseUrl + '?api_key=' + str(apikey)

    # we will want to add some inputs to our complete url
    urlData = '&data[0]=value'
    urlFreq = '&frequency=hourly'
    urlStart = '&start=' + str(start_time) + 'T00'  # format: 2022-10-23T00
    urlFacet = '&facets[fueltype][0]=' + str(fueltype)

    # concatenate to get main url
    url = baseUrl + urlData + urlFacet + urlFreq + urlStart

    r = requests.get(url=url)  # store url request as variable r
    data = r.json()  # convert our request into json format
    entries = data['response']['data']  # only grabbing data aspect of return
    df = pd.DataFrame(data=entries)  # converting our data into a pandas df
    df.reset_index(drop=True)  # resetting df index
    # df['period'] = pd.to_datetime(df['period'])  # convert period type

    return df  # return our now transformed df


def daily_energy_gen_data(start, end, fueltype, apikey, respondent):
    # base url
    baseUrl = 'https://api.eia.gov/v2/electricity/rto/daily-fuel-type-data/data/'
    baseUrl = baseUrl + '?api_key=' + str(apikey)

    # we will want to add some inputs to our complete url
    urlData = '&data[0]=value'
    urlFreq = '&frequency=daily'
    urlStart = '&start=' + str(start)  # format: 2022-10-23T00
    urlEnd = '&end=' + str(end)  # format: 2023-10-23T00
    urlFacet = '&facets[fueltype][0]=' + str(fueltype) + \
               '&facets[respondent][0]=' + str(respondent)

    # concatenate to get main url
    url = baseUrl + urlData + urlFacet + urlFreq + urlStart + urlEnd

    r = requests.get(url=url)  # store url request as variable r
    data = r.json()  # convert our request into json format
    entries = data['response']['data']  # only grabbing data aspect of return
    df = pd.DataFrame(data=entries)  # converting our data into a pandas df
    df.reset_index(drop=True)  # resetting df index
    # df['period'] = pd.to_datetime(df['period'])  # convert period type

    return df  # return our now transformed df



def combine_dfs(dfs):
    combined_df = pd.concat(dfs, axis=0, ignore_index=True)
    return combined_df

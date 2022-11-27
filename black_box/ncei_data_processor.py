import os
import requests
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

# grabbing our api key if necessary
apiKey = os.environ.get('nceiKey')


def grab_ncei_data(dataType, stations, start, end):

    '''
    :param dataType:
    :param stations:
    :param start:
    :param end:
    :return:
    '''

    # predefined url that will be used to request data
    baseUrl = 'https://www.ncei.noaa.gov/access/services/data/v1/?'

    # additional elements of the url
    dataSet = 'dataset=' + 'daily-summaries'
    dataType = '&dataTypes=' + str(dataType)  # 'AWND,WSF2,WS5'
    stations = '&stations=' + str(stations)  # 'USW00094846,USW00014925'
    startDate = '&startDate=' + str(start)  # '2015-01-01'  # YYYY-MM-DD
    endDate = '&endDate=' + str(end)  # '2020-01-01'
    units = '&units=' + 'standard'
    set_format = '&format=' + 'json'

    # this will be the main url that will be used in our GET request
    url = baseUrl + dataSet + dataType + stations + startDate + endDate + \
          units + set_format

    # process the url data
    r = requests.get(url=url)
    data = r.json()
    df = pd.DataFrame(data=data)

    # converting out dict
    convert_dict = {
        'AWND': float,
        'TMAX': float,
        'TAVG': float,
        'TMIN': float,
        'PRCP': float
    }

    # converting col values to float types
    df = df.astype(convert_dict)

    return df


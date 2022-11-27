import os
import requests

# storing our api key
api_key = os.environ.get('nsrdbKey')
print(api_key)

# base url
url = "http://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.json?api_key="
url = url + api_key

print(url)

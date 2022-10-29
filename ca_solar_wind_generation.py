from black_box.eia_data_processor import *
import os
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
pd.set_option('display.max_columns', None)


# some params related to the framework of pdf output that we will need
rc('mathtext', default='regular')
plt.rcParams["figure.autolayout"] = True


# grabbing our api key
api_key = os.environ.get('eiaAPI')

# setting up some date variables to use
today = date.today()
currentDate = today.strftime('%m_%d_%y')
startDate = today - relativedelta(years=5)
eiaStartDate = startDate.strftime('%Y-%m')



# base url
baseUrl = 'https://api.eia.gov/v2/electricity/facility-fuel/data/'
baseUrl = baseUrl + '?api_key=' + str(api_key)

# we will want to add some inputs to our complete url
urlData = '&data[0]=generation&data[1]=gross-generation'
urlFreq = '&frequency=monthly'
urlStart = '&start=' + str(eiaStartDate)
urlFacet = '&facets[fuel2002][0]=SUN&facets[fuel2002][1]=WND&facets[state][' \
           '0]=CA'

# concatenate to get main url
mainUrl = baseUrl + urlData + urlFacet + urlFreq + urlStart
print(mainUrl)

# storing our get request as a df variable
df = grab_eia_data(url=mainUrl)

# convert our new df data into csv
df.to_csv('./data_files/ca_solar_wind_gen_data.csv', index=False)

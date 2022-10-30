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
startDate = today - relativedelta(days=7)
eiaStartDate = startDate.strftime('%Y-%m-%d')

# checking df now
# fueltypes: 'SUN' or 'WND'
sun_df = daily_energy_gen_data(start=eiaStartDate, fueltype='SUN',
                               apikey=api_key)

# printing our our data as csv file
sun_df.to_csv('./data_files/us_daily_sun_gen.csv', index=False)

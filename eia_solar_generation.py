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
startDate = today - relativedelta(years=7)
eiaStartDate = startDate.strftime('%Y-%m')

# storing our get request as a df variable
df = sun_energy_gen_data(state='CA', start_date=eiaStartDate)
print(df)

# convert our new df data into csv
# df.to_csv('./data_files/ca_solar_wind_gen_data.csv', index=False)

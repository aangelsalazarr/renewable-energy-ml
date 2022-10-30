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
startDate = today - relativedelta(years=3)
eiaStartDate = startDate.strftime('%Y-%m')

# storing our get request as a df variable
ca_sun_df = sun_energy_gen_data(state='CA', start_date=eiaStartDate)
tx_sun_df = sun_energy_gen_data(state='TX', start_date=eiaStartDate)

# combine dfs into a list
dfs = [ca_sun_df, tx_sun_df]

# iterate and concatenate dfs into one
combined_df = combine_dfs(dfs=dfs)

# print out as csv file
combined_df.to_csv('./data_files/top_five_sun_gen_data.csv', index=False)



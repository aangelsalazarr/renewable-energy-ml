from black_box.nsrdb_data_processor import *
from black_box.ncei_data_processor import *
from black_box.eia_data_processor import *
from black_box.general_functions import *
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib import rc


# some params related to the framework of output that we will need
rc('mathtext', default='regular')
plt.rcParams["figure.autolayout"] = True
pd.set_option('display.max_columns', None)

# setting up params for our data_visuals
sns.set(font_scale=0.5)
sns.set_style('dark')

# storing our api keys
nsrdb_key = os.environ.get('nsrdbKey')
eia_key = os.environ.get('eiaKey')

# attributes we want to request from NSRDB
attributes = 'ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle'

# first thing we want to process is data related to solar irradiance, NSRDB
solar_rad = grab_nsrdb_data(year='2019',
                            email='aangelsalazarr@gmail.com',
                            lat='29.758938',
                            long='-95.367697',
                            atts=attributes,
                            interval='60',
                            name='Angel+Salazar',
                            key=nsrdb_key)

# second, let's process weather data for Houston, TX for 2019-2020, NCEI
# temp average, min, max, avg wind speed, precipitation
data_type = 'TAVG,TMAX,TMIN,AWND,PRCP'

# houston william hobby airport and houston intercontinental airport
htx_stations = 'USW00012918,USW00012960'

# start and end dates of data set in YYYY-MM-DD
start = '2019-01-01'
end = '2020-01-01'

# using our function to grab data
weather_df = grab_ncei_data(dataType=data_type, stations=htx_stations,
                            start=start, end=end)

# third, let's grab solar generation data from eia
solar_gen_df = daily_energy_gen_data(start='2019-01-01',
                                     end='2020-01-01',
                                     fueltype='SUN',
                                     apikey=eia_key,
                                     respondent='TEX')


# converting out data into csv output for observation
weather_df.to_csv('./data_files/htx_2019_ncei_weather_data.csv', index=False)
# converting solar rad to csv file to be stored
solar_rad.to_csv('./data_files/htx_2019_nsrdb_data.csv', index=False)
# converting solar generation to csv files to be stored
solar_gen_df.to_csv('./data_files/htx_2019_eia_solar_gen_data.csv', index=False)


# let's visualize our data, beginning with weather data
fig1 = plt.figure()
awnd = sns.lineplot(data=weather_df, x='DATE', y='AWND')

fig2 = plt.figure()
tavg = sns.lineplot(data=weather_df, x='DATE', y='TAVG')

fig3 = plt.figure()
precip = sns.lineplot(data=weather_df, x='DATE', y='PRCP')

fig4 = plt.figure()
solar_gen = sns.lineplot(data=solar_gen_df[solar_gen_df['timezone'] ==
                                           'Central'],
                         x='period',
                         y='value')

fig5 = plt.figure()
solar_rad = sns.lineplot(data=solar_rad[(solar_rad['Month'] == 1) & (
    solar_rad['Day'] <= 15)],
                         x='period',
                         y='GHI')

plt.xticks(rotation=90)

# saving all our graphs
filename = './data_visuals/htx_2019_data_visuals.pdf'

save_multi_image(filename)





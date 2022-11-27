from black_box.nsrdb_data_processor import *
from black_box.ncei_data_processor import *
from black_box.eia_data_processor import *
import os

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


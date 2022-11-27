from black_box import nsrdb_data_processor as ndp
import os


# storing our api key
api_key = os.environ.get('nsrdbKey')

# attributes we want to request
attributes = 'ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle'

# first thing we want to process is data related to solar irradiance
solar_rad = ndp.grab_nsrdb_data(year='2019',
                                email='aangelsalazarr@gmail.com',
                                lat='29.758938',
                                long='-95.367697',
                                atts=attributes,
                                interval='60',
                                name='Angel+Salazar',
                                key=api_key)

# converting solar rad to csv file to be stored
solar_rad.to_csv('./data_files/htx_2019_nsrdb_data.csv', index=False)

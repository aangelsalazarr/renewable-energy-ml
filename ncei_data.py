from black_box.ncei_data_processor import grab_ncei_data

# grabbing temperature data for texas by setting params first
# temp average, min, max, avg wind speed, precipitation
data_type = 'TAVG,TMAX,TMIN,AWND,PRCP'

# houston william hobby airport and houston intercontinental airport
htx_stations = 'USW00012918,USW00012960'

# start and end dates of data set in YYYY-MM-DD
start = '2019-01-01'
end = '2020-01-01'

# using our function to grab data
htx_df = grab_ncei_data(dataType=data_type, stations=htx_stations,
                          start=start, end=end)

# converting out data into csv output for observation
htx_df.to_csv('./data_files/htx_weather_data_2019_to_2020.csv', index=False)
import pandas as pd
import altair as alt
import numpy as np
from scipy import stats
base_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/"
flights = pd.read_csv("{}flights/flights.csv".format(base_url))
#airlines = pd.read_csv("{}airlines/airlines.csv".format(base_url))
#airports = pd.read_csv("{}airports/airports.csv".format(base_url))
#planes = pd.read_csv("{}planes/planes.csv".format(base_url))
#weather = pd.read_csv("{}weather/weather.csv".format(base_url))

#print(flights)
#print(flights.dtypes)
#print(flights.info())

#jan1 = flights.query('month == 1 & day == 1')
#print(jan1)

#The following code finds all flights that departed in November or December:
nov1 = flights.query('month == 11 | month == 12')
nov1 = nov_dec = flights.query('month in [11, 12]')


delay = flights.query('arr_delay > 120 | dep_delay > 120')
delay = flights.query('arr_delay <= 120 | dep_delay <= 120')




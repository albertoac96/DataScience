import pandas as pd

base_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/"
flights = pd.read_csv("{}flights/flights.csv".format(base_url))

print("A. Had an arrival delay of two or more hours")
arrival = flights.query('arr_delay >= 120')
print(arrival)

print("B. Flew to Houston (IAH or HOU)")
flew = flights.query('dest in ["IAH", "HOU"]')
print(flew)

print("C. Were operated by United UA, American AA, or Delta D")
operated = flights.query('carrier in ["AA", "DL","UA"]')
print(operated)

print("D. Departed in summer (July, August, and September)")
summer = nov_dec = flights.query('month in [7, 8, 9]')
print(summer)

print("E. Arrived more than two hours late, but didn’t leave late")
late = flights.query('arr_delay > 120 & dep_delay <= 0')
print(late)

print("F. Were delayed by at least an hour, but made up over 30 minutes in flight")
hours = flights.query('dep_delay >= 60 & dep_delay - arr_delay > 30')
print(hours)

print("G. Departed between midnight and 6am (inclusive)")
g = flights.query('dep_time <= 600 | dep_time == 2400')
print(g)
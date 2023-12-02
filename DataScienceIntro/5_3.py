import pandas as pd

base_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/"
flights = pd.read_csv("{}flights/flights.csv".format(base_url))


#5.3.1
#How could you use arrange() to sort all missing values to the start? (Hint: use is.na()).
print("How could you use sort() to sort all missing values to the start? (Hint: use isna()).")
a = flights.sort_values(by=['dep_time'], na_position='first')
print(a)

print("Sort flights to find the most delayed flights. Find the flights that left earliest.")
b = flights.sort_values(by=['dep_delay'], ascending=False)
b2 = flights.sort_values(by=['dep_delay'], ascending=True)
print(b)
print(b2)

print("Sort flights to find the fastest (highest speed) flights.")
c = flights.sort_values(by=['air_time'], ascending=True)
#Another definition of the “fastest flight” is the flight with the highest average ground speed. 
#The ground speed is not included in the data, but it can be calculated from the distance and air_time of the flight.
print(c)

print("Which flights travelled the farthest? Which travelled the shortest?")
d = flights.sort_values(by=['distance'], ascending=False)
d2 = flights.sort_values(by=['distance'], ascending=True)
print(d)
print(d2)
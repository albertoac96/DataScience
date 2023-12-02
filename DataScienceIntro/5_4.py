import pandas as pd

base_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/"
flights = pd.read_csv("{}flights/flights.csv".format(base_url))

#Brainstorm as many ways as possible to select dep_time, dep_delay, arr_time, and arr_delay from flights.
a1 = flights.filter(['dep_time', 'dep_delay', 'arr_time', 'arr_delay'])
a2 = flights.loc[:, ['dep_time', 'dep_delay', 'arr_time', 'arr_delay']]
a = a1.rename(columns = {'dep_time': 'tiempo_salida', 'dep_delay':'retraso_salida', 'arr_time': 'tiempo_llegada', 'arr_delay':'retraso_llegada'})
print(a)

#What happens if you include the name of a variable multiple times in a select() [filter()] call?

#What does the any_of() function do? Why might it be helpful in conjunction with this vector?

#Does the result of running the following code surprise you? How do the select helpers deal with case by default? How can you change that default?
flights.filter(regex = "TIME")


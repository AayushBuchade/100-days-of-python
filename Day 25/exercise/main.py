import os
import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# def main():
#     with open("weather_data.csv") as file:
#         data = csv.reader(file)
#         temperatures = [int(row[1]) for row in data if row[1] != 'temp']
#
#     print(temperatures)
#
# main()

temperatures = pandas.read_csv(f'{current_dir}/weather_data.csv')
    print(temperatures['temp'])
    temperatures_dict = temperatures.to_dict()
    print(temperatures_dict)
    temperatures_list = temperatures['temp'].to_list()
    print(temperatures_list)

    # data manipulation
    average_temperature = round(temperatures.temp.mean(), 2)
    print(average_temperature)


import pandas as pd


temperatures = pd.read_csv("../weather_data.csv")
print(temperatures["temp"])

temperatures_dict = temperatures.to_dict()
print(temperatures_dict)

temperatures_list = temperatures["temp"].to_list()
print(temperatures_list)

average_temperature = round(temperatures["temp"].mean(), 2)
print(average_temperature)


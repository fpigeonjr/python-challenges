# OBJECTIVE: Display statistics, table, and histogram of a set of cities and population of each city.

# prompt user for title of the data and output to the user
from __future__ import division
title = input("Enter a title for the data: ")
print(f'You entered: {title}')

# prompt user for headers of the two columns of the table
colOneHeader = input("Enter the column 1 header:")
print(f'You entered: {colOneHeader}')
colTwoHeader = input("Enter the column 2 header:")
print(f'You entered: {colTwoHeader}')

# TODO: prompt user for data points, string, int for city and population
cityData = []
cityPop = []
isDone = False
while(isDone != True):
    dataInput = input("Enter a data point('done to stop input): ")
    if(dataInput.lower() == 'done'):
        isDone = True
    else:
        name, pop = dataInput.split(',')
        print(f'City: {name}')
        print(f'Population: {pop}')
        dataPoint = {str(name), str(pop)}
        cityData.append(dataPoint)
        cityPop.append(int(pop))

#  output min, max, and mean of the population data
# https://stackoverflow.com/questions/27009247/python-find-min-max-and-average-of-a-list-array


def cityStatistics(cityPop):
    maxValue = max(cityPop)
    minValue = min(cityPop)
    avgValue = sum(cityPop)/len(cityPop)
    print('')
    print('Population Statistics')
    print(f'Minimum: {minValue}')
    print(f'Maximum: {maxValue}')
    print(f'Mean: {avgValue:.3f}')
    print('')


def cityTable(cityData, title, colOneHeader, colTwoHeader):
    print(title)
    print(f'{colOneHeader}   |   {colTwoHeader}')
    print('-----------------------------------------')
    for pop, city in cityData:
        print(f'{city}    |    {pop}')

# uncommment to debug
# print(cityPop)
# print(cityData)


cityStatistics(cityPop)
# TODO: output data in a formatted table
cityTable(cityData, title, colOneHeader, colTwoHeader)
# TODO: output data in a histogram; print one user-specified char for 100k peeps

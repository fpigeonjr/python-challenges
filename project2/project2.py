# OBJECTIVE: Display statistics, table, and histogram of a set of cities and population of each city.
# prompt user for title of the data and output to the user
title = input("Enter a title for the data: ")
print(f'You entered: {title}')
# prompt user for headers of the two columns of the table
colOneHeader = input("Enter the column 1 header:")
print(f'You entered: {colOneHeader}')
colTwoHeader = input("Enter the column 2 header:")
print(f'You entered: {colTwoHeader}')
# TODO: prompt user for data points, string, int for city and population
citydata = []
name, pop = input("Enter a data point: ").split(',')
pop = int(pop)
citydata.append({name, pop})
name, pop = input("Enter a data point: ").split(',')
pop = int(pop)
citydata.append({name, pop})
# cityOne = {'name': 'San Antonio', 'population': 100000}
# cityTwo = {'name': 'Houston', 'population': 300000}
# cityThree = {'name': 'Dallas', 'population': 600000}
# citydata.append(cityOne)
# citydata.append(cityTwo)
# citydata.append(cityThree)
print(citydata)


# TODO: output min, max, and mean of the population data
# TODO: output data in a formatted table
# TODO: output data in a histogram; print one user-specified char for 100k peeps

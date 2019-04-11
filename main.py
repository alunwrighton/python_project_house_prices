# create class and methods to read and extract data
# create method to establish mean, median and std.dev of data
# extract mean, median, std dev, top 10 and bottom 10 of data

from data_file_reader import *
from stat_analysis import *
import statistics


worksheet1 = DataFileReader("house_price_data.xlsx")
data2 = worksheet1.convert_to_list()
print(data2)

print("---------------------------------------------------------")

# mean
# First we will convert the tuples in the list so that the output is one long list
# the code below accesses xth item in tuple t in data2 and appends it to the new list tuple_to_list

calling_stats_on_data = StatAnalysis(data2)

calling_stats_on_data1 = calling_stats_on_data.tuple_to_list(data2)
print(calling_stats_on_data1)

# Since calling_stats_on_data1 contains all values (including years) we need to sum all years and take that away from sum of list

sum1993 = 1993
for i in range (1994,2018):
    sum1993 += i

sum_of_years = sum1993

# sum_of_years = sum1993 = 50125

print("---------------------------------------------------------")

mean = (sum(calling_stats_on_data1) - sum_of_years)/((len(calling_stats_on_data1)/2))

print("The mean of the house prices is: " + str(floor(mean)))

print("The length of the tuple_to_list is: " + str(len(calling_stats_on_data1)))

# median

# the index runs from 0-49, with a length of 50 values. the value associated with index 25 is the median

median = calling_stats_on_data1[ceil(int(len(calling_stats_on_data1)/2))]

print("The median of the house price is: " + str(floor(median)))

# extracting house prices alone from tuple_to_list and appending them to the list 'li'

li = []
count = 0
for i in calling_stats_on_data1:
    if count % 2 == 1:
        li.append(i)
    count += 1

print("The list of house price values on their own (without years attached) is as follows: " + str(li))

# standard deviation
# using statistics.stdev module

standard_deviation = statistics.stdev(li)

print("The standard deviation of the house price is: " + str(standard_deviation))

# top 10

top_10_base = sorted(li)

top_10 = top_10_base[(len(top_10_base)-10):]
print("The top 10 house prices are as follows: " + str(top_10))

# bottom 10

bottom_10_base = sorted(li)

bottom_10 = bottom_10_base[:10]
print("The bottom 10 house prices are as follows: " + str(bottom_10))
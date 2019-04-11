# Here is the module where we define mean, median and standard deviation methods
# to be called upon when reading the excel file

from math import *
from statistics import *

class StatAnalysis:

    def __init__(self, data1):
        self.data1 = data1

    #BELOW
    def tuple_to_list(self, data1):
        self.data1 = data1
        tuple_t_l = []
        for t in data1[1:]:
            for x in t:
                tuple_t_l.append(x)
        return tuple_t_l

    def average_value(self, data1):
        return sum(data1)/len(data1)
        # counter = 0
        # for i in self.data1:
        #     counter += i[1]
        # return counter/len(self.data1)

    def median_value(self, data1):
        self.data1 = data1
        for i in self.data1:
            if int(len(self.data1))%2 == 0:
                return (i[int(len(self.data1))/2])
            else:
                print("error")
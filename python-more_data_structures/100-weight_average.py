#!/usr/bin/python3
def weight_average(my_list=[]):
    weight_tot = list(map(lambda x: x[0] * x[1], my_list))
    weights = sum([i[1] for i in my_list])
    return sum(weight_tot) / weights

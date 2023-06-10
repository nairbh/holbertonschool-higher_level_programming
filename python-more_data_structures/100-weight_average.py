#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_score = 0
    sum_weight = 0

    for score, weight in my_list:
        sum_score += score * weight
        sum_weight += weight
    average = sum_score / sum_weight
    return average

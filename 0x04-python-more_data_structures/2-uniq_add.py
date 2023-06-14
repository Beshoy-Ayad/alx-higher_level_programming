#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set()
    for element in my_list:
        uniq_set.add(element)
    sum = 0
    for element in uniq_set:
        sum += element
    return sum

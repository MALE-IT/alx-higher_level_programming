#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = my_list[:]
    for count, num in enumerate(my_list):
        boolist[count] = num % 2 == 0
    return boolist

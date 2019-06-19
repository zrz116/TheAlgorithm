#!/usr/bin/env python
# -*-coding:utf-8 -*-
import math
def binary_search(list, num):
    low = 0
    high = len(list) - 1
    #Number of records
    j = 0
    while(low<=high):
        mid = math.floor((low + high) / 2)
        if list[mid] == num:
            j = j + 1
            return j
        if list[mid] < num:
            low = mid + 1
            j = j + 1
        else:
            high = mid - 1
            j = j + 1
    return None

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binary_search(my_list, 17))
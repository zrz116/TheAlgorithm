#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
This is my own independent work.
"""
def babble_sort(list):
    flag = 1
    while(flag):
        flag = 0
        for i in range(0, len(list)-1):
            if list[i] > list[i+1]:
                t = list[i]
                list[i] = list[i+1]
                list[i+1] = t
                flag = 1
    return list

list = [5, 3, 1, 2, 4, 1, 5]
print(babble_sort(list))
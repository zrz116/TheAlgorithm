#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
This is my own independent work, without reference to any other people's programs.
"""

def insertion_sort(list):
    N = len(list)
    for j in range(1, N):
        for i in range(0, j):
            if list[j] < list[i]:
                t = list[i]
                list[i] = list[j]
                list[j] = t
    return list

list = [5, 3, 1, 2, 4]
print(insertion_sort(list))

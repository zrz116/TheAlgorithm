#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
This is the program of 'Algorithm Illustration'
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [j for j in arr[1:] if j >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [5, 6, 1, 3, 7, 2, 4, 10, 8]
print(quick_sort(arr))


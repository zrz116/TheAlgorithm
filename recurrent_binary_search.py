#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
递归二分查找算法（自己编写）
"""

def recurrent_binary_search(arr, num, low, high, mid, j):
    if arr[mid] == num:
        j = j + 1       #j：查找次数
        return num, j
    elif arr[mid] > num:
        high = mid - 1
        mid = (low + high) // 2
        j = j + 1
        return recurrent_binary_search(arr, num, low, high, mid, j)
    else:
        low = mid + 1
        mid = (low + high) // 2
        j = j + 1
        return recurrent_binary_search(arr, num, low, high, mid, j)


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(recurrent_binary_search(my_list, 17, low=0, high=len(my_list)-1, mid=(len(my_list)-1) // 2, j=0))
#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
参考代码：https://github.com/TheAlgorithms/Python/blob/master/sorts/merge_sort.py
自己没有写出来归并排序的代码...
"""

def merge(arr):
    def merge_sort(left, right):
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return result + left + right
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge_sort(merge(arr[:mid]), merge(arr[mid:]))

arr = [5, 7, 3, 9, 1, 10, 4, 6, 2, 8]
print(merge(arr))
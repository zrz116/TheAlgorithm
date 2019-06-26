#!/usr/bin/env python
# -*-coding:utf-8 -*-
def simple_merge(arr):
    low = 0
    mid = 0
    A = arr.copy()
    A1 = A[0:len(arr)//2]
    A2 = A[len(arr)//2:len(arr)]
    for k in range(0, len(arr)):
        if low > mid:
            arr[k] = A2[mid]
            mid = mid + 1
        elif mid > low:
            arr[k] = A1[low]
            low = low + 1
        elif A1[low] < A2[mid]:
            arr[k] = A1[low]
            low = low + 1
        elif A1[low] > A2[mid]:
            arr[k] = A2[mid]
            mid = mid + 1
    return arr

arr = [1, 3, 5, 7 ,9, 11, 2, 4, 6, 8, 10, 12]
print(simple_merge(arr))

"""
这个程序根据《算法》中描述的原地归并算法编写，但是只实现了偶数长度的序列...奇数长度序列测试失败...欢迎批评指正
"""
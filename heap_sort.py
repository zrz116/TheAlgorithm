#!/usr/bin/env python
# -*-coding:utf-8 -*-
import numpy as np

def sink(arr, e, begin, end):
    i, j = begin, begin * 2
    while j < end:
        if j + 1 < end and np.less(arr[j], arr[j + 1]):
            j += 1
        if e > arr[j]:
            break
        arr[i] = arr[j]
        i, j = j, j * 2 + 1
    arr[i] = e
    return arr

def build_heap(arr):
    end = len(arr)
    for i in range(end // 2 - 1, 0, -1):
        sink(arr, arr[i], i, end)
    return arr

def exch(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


def heap_sort(arr):
    arr_heap = build_heap(arr)
    N = len(arr) - 1
    while N > 1:
        exch(arr, 1, N)
        N = N - 1
        arr = sink(arr_heap, arr_heap[1], 1, N)
    return arr

arr = ['-', 5, 6, 8, 1, 2, 4, 9]
print(build_heap(arr))
print(heap_sort(arr))

#!/usr/bin/env python
# -*-coding:utf-8 -*-

'''
This is my independent program
'''

def select_sort(list):
    length = len(list) - 1
    for i in range(length):
        j = i + 1
        while(j <= length):
            if list[i] > list[j]:
                t = list[i]
                list[i] = list[j]
                list[j] = t
                j = j + 1
            else:
                j = j + 1
    return list

list = [5, 3, 1, 1, 2]
print(select_sort(list))

'''
This is the program of 'Algorithm Illustration'
'''

def findsmallest(arr):

    '''
    Finding the smallest number in array
    '''

    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionsort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

list = [5, 3, 1, 1, 2]
print(selectionsort(list))

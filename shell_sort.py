#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
This is my own independent work, without reference to any other people's programs.
"""

def shell_sort(list):
    increment = (len(list) // 2)
    N = increment
    n = 0
    while(increment >= 1):
        while(n<increment):
            for j in range(N, len(list), increment):
                for i in range(n, j, increment):
                    if list[j] < list[i]:
                        t = list[i]
                        list[i] = list[j]
                        list[j] = t
            N = N + 1
            n = n + 1
        increment = increment // 2
        N = 1
        n = 0
    return list

list = [5, 3, 1, 9, 4, 6, 2, 8, 1, 10, 5, 23]
print(shell_sort(list))
#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
基于堆的优先队列的实现
程序的编写参考了《算法》与网上教程（https://blog.csdn.net/qq_34840129/article/details/80635361）
"""

import numpy as np

class HeapPriQueueError(ValueError):
    pass
class Heap_Pri_Queue(object):
    def __init__(self, elems=[]):
        self._elems = list(elems)
        if self._elems:
            self.buildheap()

    def is_empty(self):
        return self._elems is []

    def peek(self):   #取出堆顶元素，但不删除
        if self.is_empty():
            raise HeapPriQueueError("in pop")
        return self._elems[1]

    def enqueue(self, e):   #入队操作，在末尾增加一个元素
        self._elems.append(e)  # 此时，总的元素的长度增加了1位
        self.swim(e, len(self._elems) - 1)  #将元素上浮到合适位置

    def swim(self, e, last):  # 上浮
         elems, i, j = self._elems, last, last // 2  # j为last位置的父结点
         while i > 1 and np.less(elems[j], e):  # 如果需要插入的元素大于当前的父结点的值

             elems[i] = elems[j]  # 则将父结点的值下放到其子结点中去
             i, j = j, (j - 1) // 2  # 更新i为当前父结点的位置，j更新为当前父结点的父结点的位置
         elems[i] = e  # 如果i已经更新为1了，直接将e的值赋给位置1.或者需要插入的元素
                         # 大于当前父结点的值，则将其赋给当前父结点的子结点

    def dequeue(self):
        if self.is_empty():
            raise HeapPriQueueError("in pop")
        elems = self._elems
        e0 = elems[1]  # 根结点元素
        e = elems.pop()  # 将最后一个元素弹出，作为一个新的元素经过比较后找到插入的位置，以维持队序
        if len(elems) > 0:
            self.sink(e, 1, len(elems))
        return e0

    def sink(self, e, begin, end):  # 下沉
        elems, i, j = self._elems, begin, begin * 2  # j为i的左子结点
        while j < end:
            if j + 1 < end and np.less(elems[j], elems[j+1]):  # 如果左子结点小于右子结点
                j += 1  # 则将j指向右子结点，将j指向较大元素的位置
            if e > elems[j]:  # j已经指向两个子结点中较大的位置，
                break  # 如果插入元素e大于j位置的值，则为3者中最大的
            elems[i] = elems[j]  # 能执行到这一步的话，说明j位置元素是三者中最大的，则将其上移到父结点位置
            i, j = j, j * 2 + 1  # 更新i为被上移为父结点的原来的j的位置，更新j为更新后i位置的左子结点
        elems[i] = e  # 如果e已经是某个子树3者中最大的元素，则将其赋给这个子树的父结点
                        # 或者位置i已经更新到叶结点位置，则将e赋给这个父结点

    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2 - 1, 0, -1):  # 初始位置设置为end//2 - 1,如果end=len(elems)-1,则初始位置为(end+1)//2-1
            self.sink(self._elems[i], i, end)


if __name__ == "__main__":
    temp = Heap_Pri_Queue(['-', 5, 6, 8, 1, 2, 4, 9])
    print(temp._elems)
    temp.dequeue()
    print(temp._elems)
    temp.enqueue(10)
    print(temp._elems)
    print(temp.peek())


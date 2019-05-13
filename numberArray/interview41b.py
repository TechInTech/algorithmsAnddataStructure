# -*- coding:utf-8 -*-
"""数据流中的中位数，并定义堆方法
"""
from heapq import *

class Heap:
    def __init__(self, tp=1):
        """tp=1(default), 为堆的类别，当tp=1时，Heap为小堆，当tp=-1时，Heap为大堆
        """
        self.data = []
        self.tp = tp

    def __len__(self):
        return len(self.data)

    def insert(self, num):
        heappush(self.data, num * self.tp)

    def pop(self):
        return heappop(self.data) * self.tp

    def get_top(self):
        return nsmallest(1, self.data)[0] * self.tp


class Solution_41b(object):
    def __init__(self):
        self.total = 0
        self.min_heap = Heap()
        self.max_heap = Heap(tp=-1)

    def add_num(self, num):
        self.total += 1
        if (self.total == 1) or (num >= self.min_heap.get_top()):
            self.min_heap.insert(num)
        else:
            self.max_heap.insert(num)
        while len(self.max_heap) > len(self.min_heap):
            self.min_heap.insert(self.max_heap.pop())
        while (len(self.min_heap) - len(self.max_heap)) > (self.total % 2):
            self.max_heap.insert(self.min_heap.pop())

    def get_median(self):
        if self.total == 0:
            return None
        if self.total % 2 == 0:
            return (self.min_heap.get_top() + self.max_heap.get_top()) / 2.0
        else:
            return self.max_heap.get_top()

def main():
    ls = [4,8,2,6,3,9,1,5,0,7]

    s41 = Solution_41b()

    for i in ls:
        s41.add_num(i)

    print('The median is: ', s41.get_median())

if __name__ == '__main__':
    main()

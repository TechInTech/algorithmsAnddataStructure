# -*- coding:utf-8 -*-
"""数据流中的中位数
"""
from heapq import *

class Solution_41(object):
    def __init__(self):
        self.heaps = [], []

    def add_num(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def find_median(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


def main():
    ls = [4,8,2,6,3,9,1,5,0,7]

    s41 = Solution_41()

    for i in ls:
        s41.add_num(i)

    print('The median is: ', s41.find_median())

if __name__ == '__main__':
    main()

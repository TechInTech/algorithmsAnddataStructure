# -*- coding:utf-8 -*-
"""最小的k个数
"""
import random
from heapq import *

class Solution_40(object):
    """partition 方法
    """
    def get_least_numbers(self, nums, k):
        n = len(nums)
        if nums is None or k > n or n <= 0 or k <= 0:
            return []

        start = 0
        end = n - 1
        index = self.partition(nums, n, start, end)

        while (index != k - 1):
            if index > (k - 1):
                end = index - 1
                index = self.partition(nums, n, start, end)
            else:
                start = index + 1
                index = self.partition(nums, n, start, end)

        output = []
        for i in range(k):
            output.append(nums[i])
        return output

    def partition(self, data, length, start, end):
        if data == None or length <= 0 or start < 0 or end >= length:
            raise KeyError('Invalid Parameters.')

        index = random.randint(start, end)
        data[index], data[end] = data[end], data[index]

        small = start - 1

        for index in range(start, end):
            if data[index] < data[end]:
                small += 1
                if small != index:
                    data[index], data[small] = data[small], data[index]

        small += 1
        data[small], data[end] = data[end], data[small]
        return small

    """堆方法
    """
    def get_least_numbers_heapq(self, nums, k):
        n = len(nums)
        if nums is None or k > n or n <= 0 or k <= 0:
            return []

        heaps = []
        ret = []
        for num in nums:
            heappush(heaps, num)
        for i in range(k):
            ret.append(heappop(heaps))
        return ret

    """堆方法2
    """
    def get_least_numbers_heapq_2(self, nums, k):
        n = len(nums)
        if nums is None or k > n or n <= 0 or k <= 0:
            return []

        ret = []
        for num in nums:
            num = -num
            if len(ret) < k:
                heappush(ret, num)
            else:
                least = ret[0]
                if num > least:
                    heapreplace(ret, num)
        return sorted([-x for x in ret])

def main():
    ls = [5,0,3,7,8,9,2,4,6,1]
    # ls = []
    k = 6

    # method 1(数据较少时)
    least_num = nsmallest(k, ls)

    # method 2 (partition)
    least_num = Solution_40().get_least_numbers(ls, k)

    # method 3 (heapq)
    least_num = Solution_40().get_least_numbers_heapq(ls, k)

    # method 4 (heapq 2)
    least_num = Solution_40().get_least_numbers_heapq_2(ls, k)

    print(least_num)


if __name__ == '__main__':
    main()

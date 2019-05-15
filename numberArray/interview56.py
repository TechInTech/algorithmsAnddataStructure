# -*- coding:utf-8 -*-
"""数组中出现一次的两个数字
"""

class Solution_56(object):
    def find_nums_appear_once(self, nums):
        if not nums:
            return None
        length = len(nums)
        if length < 2:
            return None
        result_or = 0
        for n in nums:
            result_or ^= n

        index_1 = self.get_bin1(result_or)
        num1, num2 = 0, 0

        for n in nums:
            if self.is_one(n, index_1):
                num1 ^= n
            else:
                num2 ^= n
        return num1, num2

    def get_bin1(self, num):
        index_1 = 0
        while (num & 1 == 0) and (index_1 < 8 * 4):
            num = num >> 1
            index_1 += 1
        return index_1

    def is_one(self, num, index_bin):
        num = num >> index_bin
        return (num & 1)


def main():
    ls = [2, 4, 3, 6, 3, 2, 5, 5]
    ret1, ret2 = Solution_56().find_nums_appear_once(ls)
    print(ret1, ret2)


if __name__ == '__main__':
    main()

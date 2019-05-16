# -*- coding:utf-8 -*-
"""数组中唯一只出现一次的数字
"""

class Solution_56b(object):
    def find_nums_appear_once(self, nums):
        if not nums:
            return None
        length = len(nums)
        if length <= 0:
            return None

        bit_sum = [0] * 32

        for i in range(length):
            bitmask = 1
            for j in range(31, -1, -1):
                bit = nums[i] & bitmask
                if bit != 0:
                    bit_sum[j] += 1
                bitmask = bitmask << 1
        result = 0
        for i in range(32):
            result = result << 1
            result += bit_sum[i] % 3
        return result


def main():
    ls = [2, 4, 3, 3, 2, 5, 5, 2, 5, 3]
    ret = Solution_56b().find_nums_appear_once(ls)
    print(ret)


if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-
""" 构建乘积数组
"""

class Solution_66(object):
    def mutiply(self, nums):
        if not nums or len(nums) < 1:
            return []

        new_nums = [1] * len(nums)

        # 从上往下累乘左半平
        for i in range(1, len(nums)):
            new_nums[i] = new_nums[i - 1] * nums[i - 1]

        # 在从下往上累乘右上半
        temp = 1
        for i in range(len(nums) - 2, -1, -1):
            temp *= nums[i + 1]
            new_nums[i] *= temp
        return new_nums


def main():
    nums = list(range(1, 5))

    result = Solution_66().mutiply(nums)
    print('乘积矩阵:', result)


if __name__ == '__main__':
    main()

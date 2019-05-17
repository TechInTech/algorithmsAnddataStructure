# -*- coding:utf-8 -*-
"""股票的最大利润
"""

class Solution_63(object):
    def max_diff(self, nums):
        if not nums or len(nums) < 2:
            return 0

        min_value = nums[0]
        max_diff = nums[1] - min_value

        for i in range(2, len(nums)):
            if nums[i - 1] < min_value:
                min_value = nums[i - 1]

            current_diff = nums[i] - min_value
            if current_diff > max_diff:
                max_diff = current_diff

        return max_diff


def main():
    nums = [9, 11, 8, 5, 7, 12, 16, 14]

    result = Solution_63().max_diff(nums)
    print('The maximum profit is %d.'%result)


if __name__ == '__main__':
    main()

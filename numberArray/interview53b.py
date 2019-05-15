# -*- coding:utf-8 -*-
"""0--n-1中缺失的数字
"""

class Solution_53b(object):
    def get_missing_number(self, nums):
        if nums is None:
            return -1
        length = len(nums)
        if length <= 0:
            return -1

        left = 0
        right = length - 1

        while left <= right:
            middle = (right + left) >> 1
            if nums[middle] != middle:
                if middle == 0 or nums[middle - 1] == middle - 1:
                    return middle
                right = middle - 1
            else:
                left = middle + 1

        if left == length:
            return length
        return -1


def main():
    ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

    result = Solution_53b().get_missing_number(ls)
    print('The index is %d.'%result)

if __name__ == '__main__':
    main()

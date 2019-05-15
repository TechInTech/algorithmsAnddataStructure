#-*- coding:utf-8 -*-
"""数组中数值和下标相等的元素
"""

class Solution_53c(object):
    def get_number_same_as_index(self, nums):
        if nums is None:
            return -1
        length = len(nums)
        if length <= 0:
            return -1

        left, right = 0, length - 1
        while left <= right:
            middle = left + ((right - left) >> 1)
            if nums[middle] == middle:
                return middle
            if nums[middle] > middle:
                right = middle - 1
            else:
                left = middle + 1
        return -1

def main():
    ls = [-3, -1, 1, 3, 5]

    result = Solution_53c().get_number_same_as_index(ls)
    print('The number is %d.'%result)

if __name__ == '__main__':
    main()

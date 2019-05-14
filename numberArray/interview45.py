# -*- coding:utf-8 -*-
"""把数组排成最小的数
"""
from functools import cmp_to_key

# py2中sort和sorted的cmp关键字在py3中已经取消了，在py3中要调用该关键字
# 必须要import functools库里面的cmp_to_key

class Solution_45(object):
    def print_min_number(self, nums):
        if nums is None:
            return
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(self.cmp))
        return 0 if nums[0] == '0' else int(''.join(nums))

    def cmp(self, x, y):
        left = x + y
        right = y + x
        if left > right:
            return 1
        elif left < right:
            return -1
        else:
            return 0

    def print_min(self, nums):
        if nums is None:
            return
        nums = list(map(str, nums))
        nums = sorted(nums, key=cmp_to_key(self.cmp))
        return int(''.join(nums))

    def print_min_2(self, nums):
        if not nums:
            return ''
        nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = int(nums[i] + nums[j])
                b = int(nums[j] + nums[i])
                if a > b:
                    nums[i], nums[j] = nums[j], nums[i]
        s = ''
        for i in range(len(nums)):
            s += nums[i]
        return int(s)


def main():
    nums = [321, 32, 3]

    # max_num = Solution_45().print_min_number(nums)
    max_num = Solution_45().print_min_2(nums)

    print('The maximum is %d'%max_num)

if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-
"""滑动窗口的最大值
"""

class Solution_59(object):
    def max_in_windows(self, nums, n):
        if not nums or len(nums) <=0 or n <= 0:
            return None

        max_in_windows = list()
        if len(nums) > n and n >= 1:
            index_ls = list()

            for i in range(n):
                while len(index_ls) > 0 and nums[i] >= nums[index_ls[-1]]:
                    index_ls.pop()
                index_ls.append(i)

            for i in range(n, len(nums)):
                max_in_windows.append(nums[index_ls[0]])

                while len(index_ls) > 0 and nums[i] >= nums[index_ls[-1]]:
                    index_ls.pop()
                if len(index_ls) > 0 and index_ls[0] <= (i - n):
                    index_ls.pop(0)
                index_ls.append(i)
            max_in_windows.append(nums[index_ls[0]])
        return max_in_windows


def main():
    nums = [2, 3, 4, 2, 6, 2, 5, 1]
    n = 3

    result = Solution_59().max_in_windows(nums, n)
    print('The maximum value are ', result)


if __name__ == '__main__':
    main()

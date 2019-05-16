# -*- coding:utf-8 -*-
"""和为s的数字
"""

class Solution_57(object):
    def find_number_with_sum(self, nums, tar_sum):
        if not nums:
            return None
        length = len(nums)
        if length < 1:
            return None

        ahead = length - 1
        behind = 0

        while ahead > behind:
            cur_sum = nums[ahead] + nums[behind]
            if cur_sum == tar_sum:
                return (nums[ahead], nums[behind])
            elif cur_sum > tar_sum:
                ahead -= 1
            else:
                behind += 1
        return None


def main():

    array = [1, 2, 4, 7, 11, 15]
    tar_sum = 15

    result = Solution_57().find_number_with_sum(array, tar_sum)
    if result:
        print('The numbers are %d and %d.'%(result[0], result[1]))
    else:
        print('There are not two numbers.')


if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-
"""数组中出现次数超过一半的数字
"""
import random
class Solution_39(object):
    G_BINPUTINVALID = False

    def get_more_half_num(self, nums):
        if len(nums) <= 0:
            return 0
        hashes = dict()
        length = len(nums)
        for n in nums:
            hashes[n] = hashes[n] + 1 if hashes.get(n) else 1
            if hashes[n] > length / 2:
                return n

    def more_than_half_num(self, nums):
        length = len(nums)
        if self.check_invalid_array(nums, length):
            return 0

        middle = length >> 1
        start = 0
        end = length - 1
        index = self.partition(nums, length, start, end)

        while index != middle:
            if index > middle:
                end = index - 1
                index = self.partition(nums, length, start, end)
            else:
                start = index + 1
                index = self.partition(nums, length, start, end)

        result = nums[middle]

        if not self.check_more_than_half(nums, length, result):
            result = 0
        return result

    def more_than_half_num_2(self, nums):
        length = len(nums)
        if self.check_invalid_array(nums,length):
            return 0

        result = nums[0]
        times = 1
        for i in range(1, length):
            if times == 0:
                result = nums[i]
                times = 1
            elif nums[i] == result:
                times += 1
            else:
                times -= 1

        if not self.check_more_than_half(nums, length, result):
            return 0

        return result

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

    """
    def partition(self, nums, low, high):
        parti = nums[low]
        while low < high:
            while low < high and nums[high] >= parti:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= parti:
                low += 1
            nums[high] = nums[low]
        nums[low] = parti
        return low
    """

    def check_invalid_array(self, nums, length):
        G_BINPUTINVALID = False

        if nums is None or length <= 0:
            G_BINPUTINVALID = True
        return G_BINPUTINVALID

    def check_more_than_half(self, nums, length, number):
        times = 0
        for i in range(length):
            if nums[i] == number:
                times += 1

        is_more_than_half = True
        if times * 2 <= length:
            G_BINPUTINVALID = True
            is_more_than_half = False

        return is_more_than_half


def main():
    array = [1, 3, 1, 0, 1, 9, 4, 3, 1, 1, 6, 1, 1]
    # mediem = Solution_39().get_more_half_num(array)

    mediem = Solution_39().more_than_half_num(array)

    print('数组中出现次数超过%d的数字为: %d'%(len(array)/2, mediem))

if __name__ == '__main__':
    main()

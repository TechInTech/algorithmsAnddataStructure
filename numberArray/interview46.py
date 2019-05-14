# -*- coding:utf-8 -*-
"""把数字翻译成字符串
"""
class Solution_46(object):
    def get_Translation(self, nums):
        """
        nums: int
        """
        if nums < 0:
            return 0
        nums_to_str = str(nums)
        return self.get_Translation_count(nums_to_str)

    def get_Translation_count(self, nums_to_str):
        length = len(nums_to_str)
        count_ls = [0] * length

        count = 0

        for i in range(length-1, -1, -1):
            count = 0
            if i < length -1:
                count = count_ls[i+1]
            else:
                count = 1
            if i < length - 1:
                digit1 = int(nums_to_str[i])
                digit2 = int(nums_to_str[i+1])
                converted = digit1*10 + digit2
                if converted >= 10 and converted <= 25:
                    if i < length - 2:
                        count += count_ls[i+2]
                    else:
                        count += 1
            count_ls[i] = count
        count = count_ls[0]
        del count_ls
        return count


def main():
    number = 12258

    result = Solution_46().get_Translation(number)

    print('There are %d methods.'%result)


if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-
"""扑克牌的顺子
"""

class Solution_61(object):
    def is_continuous(self, number):
        if not number or len(number) < 1:
            return False

        number = sorted(number)
        number_of_zero, number_of_gap = 0, 0

        number_of_zero = number.count(0)

        small = number_of_zero
        big = small + 1
        while big < len(number):
            if number[small] == number[big]:
                return False
            number_of_gap += number[big] - number[small] - 1
            small = big
            big += 1
        return False if number_of_gap > number_of_zero else True


def main():
    nums = [3, 0, 6, 7, 0]

    s61 = Solution_61()
    result = s61.is_continuous(nums)

    if result:
        print('The number is continuous.')
    else:
        print('The number is not continuous.')


if __name__ == '__main__':
    main()

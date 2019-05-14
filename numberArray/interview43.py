# -*- coding:utf-8 -*-
"""1-n整数中1出现的次数
"""
import string

class Solution_43(object):
    def number_of_1_between_1_and_n(self, n):
        number = 0
        for i in range(1, n+1):
            number += self.number_of_1(i)
        return number

    def number_of_1(self, n):
        number = 0
        while n:
            if n % 10 == 1:
                number += 1
            n = n // 10
        return number

    def solution_2(self, n):
        if n < 1:
            return 0
        if n == 1:
            return 1
        last, ans, pos = 0, 0, 1
        while n:
            num = n % 10
            n = n // 10
            ans += pos * n
            if num > 1:
                ans += pos
            elif num == 1:
                ans += (last + 1)
            last = last + num * pos
            pos *= 10
        return ans

    """
    def solution2(self, n):
        if n <= 0:
            return 0
        str_n = str(n)
        return self.calc_number(str_n)

    def calc_number(self, n):
        length = len(n)

        if n < '0' or n > '9' or length <= 0:
            return 0

        first = int(n) - int('0')

        if length == 1 and first == 0:
            return 0

        if length == 1 and first > 0:
            return 1

        # assumption n='21345'
        # num_first_digit是数字10000-19999的第一位中的数目
        num_first_digit = 0

        if first > 1:
            num_first_digit = self.power_base_10(length - 1)
        elif first == 1:
            num_first_digit = string.atoi(n) + 1

        # num_other_digit是1346-21345除第一位之外的数位中的数目
        num_other_digit = first * (length - 1) * self.power_base_10(length - 2)
        # num_recursive是1-1345中的数目
        num_recursive = self.number_of_1(n + 1)

        return num_first_digit + num_other_digit + num_recursive

    def power_base_10(self, n):
        result = 1
        for i in range(n):
            result *= 10
        return result
    """


def main():
    n = 55

    # number = Solution_43().number_of_1_between_1_and_n(n)
    number = Solution_43().solution_2(n)
    print('The numbers of 1 between 1 and %d are %d: '%(n, number))

if __name__ == '__main__':
    main()

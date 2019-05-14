# -*- coding:utf-8 -*-
"""数字序列中某一位的数字
"""
class Solution_44(object):
    def digit_at_index(self, n):
        if n < 0:
            return -1

        digit = 1
        while True:
            number = self.count_of_integers(digit)
            if n < number * digit:
                return self.digit_at_index_2(n, digit)
            n -= digit * number
            digit += 1
        return -1

    # 计算digit位的数字有多少个
    def count_of_integers(self, digit):
        """digit: 数字位数
        """
        if digit == 1:
            return 10
        count = pow(10, digit - 1)
        return 9 * count

    def digit_at_index_2(self, n, digit):
        """
        """
        number = self.begin_number(digit) + n // digit
        index_from_right = digit - n % digit
        for i in range(1, index_from_right):
            number = number // 10
        return number % 10

    def begin_number(self, digit):
        """第一个digit位数的起始数字
        """
        if digit == 1:
            return 0
        return pow(10, digit - 1)


def main():
    # 序列的第n位
    n = 1001

    result = Solution_44().digit_at_index(n)
    print('The number is %d in digit series.'% result)


if __name__ == '__main__':
    main()

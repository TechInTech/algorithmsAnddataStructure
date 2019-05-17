# -*- coding:utf-8 -*-
"""不用加减乘除做加法
"""

class Solution_65(object):
    def add(self, num1, num2):
        while num2:
            num1, num2 = (num1^num2) & 0xFFFFFFFF, ((num1 & num2)<<1) & 0xFFFFFFFF
        return num1 if num1 <= 0x7FFFFFFF else ~(a^0xFFFFFFFF)


def main():
    num1, num2 = 5, 7

    result = Solution_65().add(num1, num2)
    print('The result %d + %d is %d.'%(num1, num2, result))


if __name__ == '__main__':
    main()

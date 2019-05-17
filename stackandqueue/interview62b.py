# -*- coding:utf-8 -*-
"""圆圈中最后剩下的数字
"""

class Solution_62b(object):
    def last_remaining(self, n, m):
        if n < 1 or m < 1:
            return -1

        last = 0
        for i in range(2, n+1):
            last = (last + m)%i
        return last


def main():
    n, m = 6, 3
    result = Solution_62b().last_remaining(n, m)
    print('The last number is %d.'%result)


if __name__ == '__main__':
    main()

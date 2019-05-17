# -*- coding:utf-8 -*-
"""求1+2+...+n
"""

class Solution_64(object):
    def get_sum_1(self, n):
        return sum(range(1, n + 1))

    def get_sum_2(self, n):
        return reduce(lambda x,y: x+y, range(1, n+1))

    def get_sum_3(self, n):
        ans = n
        temp = ans and self.get_sum_3(n - 1)
        ans = ans + temp
        return ans


def main():
    n = 10

    result = Solution_64().get_sum_3(n)
    print('The sum of 1 - %d is %d.'%(n, result))


if __name__ == '__main__':
    main()

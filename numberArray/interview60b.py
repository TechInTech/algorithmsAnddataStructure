# -*- coding:utf-8 -*-
"""n个骰子的点数(基于循环求骰子点数)
"""
import copy

G_MAXVALUE = 6 # 骰子点数可自定义

class Solution_60b(object):
    def print_probability(self, number):
        if number < 1:
            return

        # probabilities = [[0] * (G_MAXVALUE * number + 1), [0] * (G_MAXVALUE * number + 1)]
        ls = [0] * (G_MAXVALUE * number + 1)
        probabilities = [ls, copy.copy(ls)]

        flag = 0
        for i in range(1, G_MAXVALUE + 1):
            probabilities[flag][i] = 1

        for k in range(2, number + 1):
            for i in range(k):
                probabilities[1 - flag][i] = 0

            for i in range(k, G_MAXVALUE * k + 1):
                probabilities[1 - flag][i] = 0
                j = 1
                while j <= i and j <= G_MAXVALUE:
                # for j in range(1, min(i+1, G_MAXVALUE+1)):
                    probabilities[1 - flag][i] += probabilities[flag][i - j]
                    j += 1
            flag = 1 - flag
        #
        total = pow(G_MAXVALUE, number)
        for i in range(number, G_MAXVALUE * number + 1):
            ratio = probabilities[flag][i]/total
            print('%d: %.4f'%(i, ratio))

        del probabilities


def main():
    n = 6

    s60 = Solution_60b()
    s60.print_probability(n)


if __name__ == '__main__':
    main()

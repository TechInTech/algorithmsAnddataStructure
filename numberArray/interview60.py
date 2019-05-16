# -*- coding:utf-8 -*-
"""n个骰子的点数(基于递归求骰子点数)
"""
G_MAXVALUE = 6

class Solution_60(object):

    def print_probability(self, number):
        if number < 1:
            return

        max_sum = number * G_MAXVALUE
        probabilities = [0] * (max_sum - number + 1)

        probabilities = self.probability(number, probabilities)

        total = pow(G_MAXVALUE, number)

        for i in range(number, max_sum + 1):
            ratio = probabilities[i - number] / total
            print('%d: %.4f'%(i, ratio))

        del probabilities

    def probability(self, number, probabilities):
        for i in range(1, G_MAXVALUE + 1):
            probabilities = self.probability_2(number, number, i, probabilities)
        return probabilities

    def probability_2(self, original, current, sum, probabilities):
        if current == 1:
            probabilities[sum - original] += 1
        else:
            for i in range(1, G_MAXVALUE + 1):
                probabilities = self.probability_2(original, current - 1, \
                    i + sum, probabilities)
        return probabilities


def main():
    n = 6

    s60 = Solution_60()
    s60.print_probability(n)


if __name__ == '__main__':
    main()

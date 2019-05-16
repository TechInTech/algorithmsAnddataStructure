# -*- coding:utf-8 -*-
"""和为s的连续正数序列
"""

class Solution_57b(object):
    def find_continuous_sequence(self, tar_sum):
        if tar_sum < 3:
            return None

        small, big = 1, 2
        middle = (1 + tar_sum) // 2
        cur_sum = small + big

        while small < middle:
            if cur_sum == sum:
                self.print_continus_sequence(small, big)

            while cur_sum > tar_sum and small < middle:
                cur_sum -= small
                small += 1

                if cur_sum == tar_sum:
                    self.print_continus_sequence(small, big)
            big += 1
            cur_sum += big

    def print_continus_sequence(self, small, big):
        for i in range(small, big + 1):
            print('%d'%i, end=', ')
        print('\n')


def main():

    tar_sum = 15

    Solution_57b().find_continuous_sequence(tar_sum)


if __name__ == '__main__':
    main()

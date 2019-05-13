# -*- coding:utf-8 -*-
"""连续子数组的最大和
"""

class Solution_42(object):
    G_INVALIDINPUT = False

    def find_greatest_sum_of_subarray(self, data):
        n = len(data)
        if data is None or n <= 0:
            G_INVALIDINPUT = True
            return 0

        G_INVALIDINPUT = False

        n_sum = 0
        n_great_sum = 0
        for i in range(n):
            if n_sum <= 0:
                n_sum = data[i]
            else:
                n_sum += data[i]
            if n_sum > n_great_sum:
                n_great_sum = n_sum
        return n_great_sum

def main():
    ls = [1, -2, 3, 10, -4, 7, 2, -5]
    n_sum = Solution_42().find_greatest_sum_of_subarray(ls)

    print('The maximam of subarray is: ', n_sum)

if __name__ == '__main__':
    main()

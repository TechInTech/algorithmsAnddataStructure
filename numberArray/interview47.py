# -*- coding:utf-8 -*-
"""礼物的最大价值
"""

class Solution_47(object):
    def get_max_value(self, array, rows, cols):
        if not array or rows <= 0 or cols <= 0:
            return 0

        max_values = [[0] * cols] * rows

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = max_values[i-1][j]
                if j > 0:
                    left = max_values[i][j-1]

                max_values[i][j] = max(left, up) + array[i][j]

        max_value = max_values[rows-1][cols-1]
        del max_values
        return max_value

    def get_max_value_2(self, array, rows, cols):
        if not array or rows <= 0 or cols <= 0:
            return 0

        max_values = [0] * cols
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = max_values[j]
                if j > 0:
                    left = max_values[j-1]

                max_values[j] = max(left, up) + array[i][j]

        max_value = max_values[cols-1]
        del max_values
        return max_value

def main():
    array = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    m, n = len(array), len(array[0])

    s47 = Solution_47().get_max_value(array, m, n)
    print('The maximum gift is %d.'%s47)

if __name__ == '__main__':
    main()

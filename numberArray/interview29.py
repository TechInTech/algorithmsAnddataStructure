# -*- coding:utf-8 -*-

"""顺时针打印矩阵
"""

class  Solution_29(object):
    def print_matrix_clock_wisely(self, matrix, rows, cols):
        if matrix is None or rows <= 0 or cols <= 0:
            return

        start = 0

        while (cols > start * 2) and (rows > start * 2):
            self.print_matrix_in_circle(matrix, rows, cols, start)
            start += 1

    def print_matrix_in_circle(self, matrix, rows, cols, start):
        endx = cols - 1 - start
        endy = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, endx+1):
            number = matrix[start][i]
            print(number)

        # 从上到下打印一列
        if start < endy:
            for i in range(start+1, endy+1):
                number = matrix[i][endx]
                print(number)

        #从右到左打印一行
        if start < endx and start < endy:
            for i in range(endx-1,start-1,-1):
                number = matrix[endy][i]
                print(number)

        # 从下到上打印一列
        if start < endx and start < (endy -1):
            for i in range(endy-1, start,-1):
                number = matrix[i][start]
                print(number)


def main():
    array = [[1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]]

    m, n = len(array), len(array[0])
    s29 = Solution_29()
    s29.print_matrix_clock_wisely(array, m, n)

if __name__ == '__main__':
    main()

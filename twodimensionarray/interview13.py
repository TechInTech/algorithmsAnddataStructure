import numpy as np
import math


def robotmove(rows, cols, threshold):
    if rows <= 0 or cols <= 0 or threshold < 0:
        raise KeyError('The matrix\'s numbers is zero!')
    check_matrix = np.full((rows, cols), fill_value=False)
    num = movingincheck(check_matrix, rows, cols, 0, 0, threshold)
    return num


def movingincheck(check_matrix, rows, cols, row, col, threshold):
    num = 0
    if check(check_matrix, rows, cols, row, col, threshold):
        check_matrix[row, col] = True

        num = 1 + movingincheck(check_matrix, rows, cols, row, col - 1, threshold) +\
            movingincheck(check_matrix, rows, cols, row - 1, col, threshold) +\
            movingincheck(check_matrix, rows, cols, row, col + 1, threshold) +\
            movingincheck(check_matrix, rows, cols, row + 1, col, threshold)
    return num


def check(check_matrix, rows, cols, row, col, threshold):
    if row >= 0 and row < rows and col >= 0 and col < cols and (count_num(row, col) < threshold) and\
            (not check_matrix[row, col]):
        return True

    return False


def count_num(row, col):
    sum_row_col = 0
    sum_row_col += sumdigits(row)
    sum_row_col += sumdigits(col)
    return sum_row_col


def sumdigits(n):
    a = len(str(n))
    if n < 10:
        return n
    else:
        Heigh = int(n / math.pow(10, a - 1))
        residual = int(n - Heigh * math.pow(10, a - 1))
        n = Heigh + sumdigits(residual)
        return n


def main():
    rows = int(input('input the rows:'))
    cols = int(input('input the cols:'))
    threshold = int(input('input the threshold:'))

    result = robotmove(rows, cols, threshold)

    print('The number of robot moving is %d' % result)


if __name__ == '__main__':
    main()

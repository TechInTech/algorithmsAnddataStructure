import numpy as np


def movingcount(threshold, rows, cols):
    if threshold < 0 or rows <= 0 or cols <= 0:
        raise KeyError('The check matrix is empty!')

    visited = np.full((rows, cols), fill_value=False)

    count = movingcountcore(threshold, rows, cols, 0, 0, visited)

    return count


def movingcountcore(threshold, rows, cols, row, col, visited):
    count = 0
    if check(threshold, rows, cols, row, col, visited):
        visited[row, col] = True

        count = 1 + movingcountcore(threshold, rows, cols, row, col - 1, visited) +\
            movingcountcore(threshold, rows, cols, row - 1, col, visited) +\
            movingcountcore(threshold, rows, cols, row, col + 1, visited) +\
            movingcountcore(threshold, rows, cols, row + 1, col, visited)
    return count


def check(threshold, rows, cols, row, col, visited):
    if row >= 0 and row < rows and col >= 0 and col < cols and (getdigits(row)
        + getdigits(col) <= threshold) and (not visited[row, col]):
        return True

    return False


def getdigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10
    return sum


def main():
    rows = int(input('input the rows:'))
    cols = int(input('input the cols:'))
    threshold = int(input('input the threshold:'))

    count = movingcount(threshold, rows, cols)

    print('The number visited is %d' % count)


if __name__ == '__main__':
    main()

import numpy as np

def hasPath(matrix, rows, cols, str_elem):
    if rows < 1 or cols < 1 or str_elem is None:
        return False
    visited = np.full((rows, cols), fill_value=False)

    str_length = len(str_elem)

    path_length = 0
    for row in range(rows):
        for col in range(cols):
            if hasPathCore(matrix, rows, cols, row, col, str_elem, path_length, visited, str_length):
                return True
    return False


def hasPathCore(matrix, rows, cols, row, col, str_elem, path_length, visited, str_length):
    if path_length == str_length:
        return True

    hasPath = False
    if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row, col] == str_elem[path_length] and not visited[row, col]:
        path_length += 1

        visited[row, col] = True

        hasPath = hasPathCore(matrix, rows, cols, row, col - 1, str_elem, path_length, visited, str_length) or \
        hasPathCore(matrix, rows, cols, row - 1, col, str_elem, path_length, visited, str_length) or \
        hasPathCore(matrix, rows, cols, row, col + 1, str_elem, path_length, visited, str_length) or \
        hasPathCore(matrix, rows, cols, row + 1, col, str_elem, path_length, visited, str_length)

        if not hasPath:
            path_length -= 1
            visited[row, col] = False

    return hasPath


def main():
    str_list = [['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
    str_mat = np.array(str_list)
    rows, cols = str_mat.shape
    str_elem = 'bfce'
    result = hasPath(str_mat, rows, cols, str_elem)

    if result:
        print('There exist a path!')
    else:
        print('There is not such path!')


if __name__ == '__main__':
    main()

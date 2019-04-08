# -*- coding:utf-8 -*-

# To judge whether an integer is in a gived two-dimension array.

def input_array():
    """In the two-dimension array, the number in each row is sorted incrementally from
    left to right, and the number in each col is sorted incrementally from up to down.
    """

    print('please input a diemension array!')
    print('A two-diemension array is gived, you can use the gived one by enter the \'n/N\', or to define a new one by enter \'y/Y\'.')
    key = input('Make you choose(y/n):')
    while key =='':
        key = input('Make you choose(y/n):')
    if key == 'y' or key == 'Y':
        print('please input the row and col of a dimension array!')
        m = int(input('The row is:'))
        n = int(input('The col is:'))
        array = []
        i = 0
        while i < m:
            line = input('please input the ' + str(i) +' row array, the col number is ' + str(n) + '(number splited with \',\'):')
            if line == '' and i < m:
                print('The array has ' + str(m) + ' row,' + ' please input the rest ' + str(m - i) + ' row!')
                continue
            if len(line) != (n + n - 1):
                print('The input number is less ' + str(n) + ' in a row, please input again!')
                continue
            data = [int(li) for li in line.split(',')]
            array.append(data)
            i += 1
        return array, m, n
    elif key == 'n' or key == 'N':
        array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
        m, n = 4, 4
        return array, m, n

def find_fun(array, val, m, n):
    i, j = 0, n - 1
    while i < m and j >= 0:
        if array[i][j] == val:
            return True, [i, j]
        elif array[i][j] > val:
            j -= 1
            continue
        elif array[i][j] < val:
            i += 1
            continue
    return False, -1

def main():
    dataarray, row, col = input_array()
    print('The input two-dimension array is:', dataarray)

    val = int(input('please input the number to search:'))

    ret, local = find_fun(dataarray, val, row, col)
    if ret:
        print('The number %d is in the two-dimension array, and the local is in %d row, %d col.'% (val, local[0], local[1]))
    else:
        print('There number %d is not in the two-dimension array.'% val)

if __name__ == '__main__':
    main()

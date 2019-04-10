# -*- coding:utf-8 -*-

import numpy as np


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_circulation(n):
    a, b = 0, 1
    while(n):
        a, b, n = b, a + b, n-1
    return a

def fibonacci_matrix(n):
    res = pow(np.matrix([[1, 1], [1, 0]]), n - 1) * np.matrix([[1], [0]])
    return int(res[0][0])


def main():
    # print('************* fibonacci_circulation *************')
    # for i in range(40):
    #     result = fibonacci_circulation(i)
    #     print(str(i)+': ' + str(result))

    # print('************* fibonacci_recursive *************')
    # for i in range(40):
    #     result = fibonacci_recursive(i)
    #     print(str(i)+': ' + str(result))

    print('************* fibonacci_matrix *************')
    for i in range(40):
        result = fibonacci_matrix(i)
        print(str(i)+': ' + str(result))


if __name__ == '__main__':
    main()

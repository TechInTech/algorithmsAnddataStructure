import numpy as np
import math

def maxproduct(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    products = np.zeros(length + 1, dtype=np.int32)
    # products = [0] * (length + 1)

    for i in range(4):
        products[i] = i

    max = 0
    for i in range(4, length + 1):
        max = 0
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if max < product:
                max = product
            products[i] = max
    max = products[length]
    return max


def maxproduct2(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    timesof3 = length // 3
    if (length - timesof3 * 3) == 1:
        timesof3 -= 1
    timesof2 = (length - timesof3*3) // 2
    return (math.pow(3, timesof3)) * (math.pow(2, timesof2))

def main():
    length = int(input('Please input the length of string:'))
    # maxpro = maxproduct(length)
    maxpro = maxproduct2(length)
    print('When the string\'s length is %d, the maximum product is %d' % (length, maxpro))


if __name__ == '__main__':
    main()

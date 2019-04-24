import numpy as np


class Solution_21(object):
    def __init__(self):
        self.front = 0
        self.rear = 0

    def recorder_odd_even(self, array, length):
        if array is None or length == 0:
            return

        self.rear = length - 1

        while self.front < self.rear:
            while self.front < self.rear and (not self.iseven(array[self.front])):
                self.front += 1

            while self.front < self.rear and self.iseven(array[self.rear]):
                self.rear -= 1

            if self.front < self.rear:
                array[self.front], array[self.rear] = array[self.rear], array[self.front]

        return array

    def iseven(self, n):
        return (n & 1) == 0

def main():
    array = list()
    temp = input('Input the elements of array:')
    while temp != '':
        array.append(int(temp))
        temp = input('Input the elements of array:')

    array = np.array(array)
    length = len(array)
    print('Before the adjusting, the array is:')
    print(array)

    solu = Solution_21()
    array = solu.recorder_odd_even(array, length)
    print('After the adjusting, the array is:')
    print(array)


if __name__ == '__main__':
    main()

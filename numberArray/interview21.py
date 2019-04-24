
import numpy as np

class Adjust_the_location_of_odd_and_even(object):
    def __init__(self):
        self.front = 0
        self.rear = 0

    def create_array(self):
        label = True
        array = list()
        while label:
            temp = input('Input the number:')
            if temp == '':
                label = False
            else:
                temp = int(temp)
                array.append(temp)
        return np.array(array)

    def init_para(self, n):
        self.rear = n - 1

    def adjust_loaction(self):
        array =self.create_array()
        n = len(array)
        self.init_para(n)

        print('Before adjusting, the array is:')
        print(array)

        while self.front < self.rear:
            if array[self.front] % 2 != 0:
                self.front += 1
            elif array[self.front] % 2 == 0:
                if array[self.rear] % 2 != 0:
                    array[self.front], array[self.rear] = array[self.rear], array[self.front]
                    self.front += 1
                else:
                    self.rear -= 1
        print('After the adjusting, the array is:')
        print(array)


def main():
    adj_function = Adjust_the_location_of_odd_and_even()

    adj_function.adjust_loaction()


if __name__ == '__main__':
    main()

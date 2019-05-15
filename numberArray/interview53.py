# -*- coding:utf-8 -*-
"""在排序数组中查找数字
"""
class SOlution_53(object):
    def __init__(self, data, k):
        self.data = data
        self.k = k
        if self.data is None:
            self.length = 0
        else:
            self.length = len(data)

    def get_first_k(self, start, end):
        if start > end:
            return -1

        middle_index = (start + end) // 2
        middle_data = self.data[middle_index]

        if middle_data == self.k:
            if (middle_index > 0 and self.data[middle_index - 1] != self.k) or \
                middle_index == 0:
                return middle_index
            else:
                end = middle_index - 1
        elif middle_data > self.k:
            end = middle_index - 1
        else:
            start = middle_index + 1
        return self.get_first_k(start, end)

    def get_last_k(self, start, end):
        if start > end:
            return -1

        middle_index = (start + end) // 2
        middle_data = self.data[middle_index]

        if middle_data == self.k:
            if (middle_index < self.length - 1 and self.data[middle_index + 1] != self.k) or \
                middle_index == self.length - 1:
                return middle_index
            else:
                start = middle_index + 1
        elif middle_data < self.k:
            start = middle_index + 1
        else:
            end = middle_index - 1
        return self.get_last_k(start, end)

    def get_number_of_k(self):
        number = 0
        if self.data is not None and self.length > 0:
            first = self.get_first_k(0, self.length - 1)
            last = self.get_last_k(0, self.length - 1)

            if first > -1 and last > -1:
                number = last - first + 1
        return number


def main():
    ls = [1, 2, 3, 3, 3, 3, 4, 5]
    k = 3

    result = SOlution_53(ls, k).get_number_of_k()

    print('The number is %d.'%result)


if __name__ == '__main__':
    main()

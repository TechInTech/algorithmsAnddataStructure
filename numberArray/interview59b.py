# -*- coding:utf-8 -*-
"""队列的最大值
"""
from queue import Queue


class Internal_Data(object):
    def __init__(self, number=None, index=None):
        self.number_ = number
        self.index_ = index


class Queue_With_Max(object):
    def __init__(self, currentindex=0):
        self.maximums = Queue()
        self.data = Queue()
        self.current_index = currentindex

    def push_back(self, number):
        while not self.maximums.isEmpty() and number >= self.maximums.back().number_:
            self.maximums.pop_back()
        internaldata = Internal_Data(number, self.current_index)
        self.data.push_back(internaldata)
        self.maximums.push_back(internaldata)
        self.current_index += 1

    def pop_front(self):
        if self.maximums.isEmpty():
            raise KeyError('The queue is empty.')
        if self.maximums.front().index_ == self.data.front().index_:
            self.maximums.pop_front()
        return self.data.pop_front()

    def max(self):
        if self.maximums.isEmpty():
            raise KeyError('The queue is Empty.')
        return self.maximums.front().number_

def main():
    nums = [2, 3, 4, 2, 6, 2, 5, 1]

    queue_max = Queue_With_Max()

    for i in nums:
        queue_max.push_back(i)

    max_result = queue_max.max()

    print('The maximum value are %d.'% max_result)


if __name__ == '__main__':
    main()

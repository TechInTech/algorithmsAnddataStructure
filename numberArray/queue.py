# -*- coding:utf-8 -*-
"""定义的队列类
"""

class Queue(object):
    def __init__(self):
        self.queue_ = list()
        self.size_ = 0

    def isEmpty(self):
        if self.size_ == 0:
            return True
        else:
            return False

    def front(self):
        if self.isEmpty():
            raise KeyError('The queue is empty.')
        return self.queue_[0]

    def back(self):
        if self.isEmpty():
            raise KeyError('The queue is empty.')
        return self.queue_[-1]

    def push_back(self, item=None):
        """
        item: 为Internal_data()
        """
        self.queue_.append(item)
        self.size_ += 1

    def push_front(self, item=None):
        """
        item: 为Internal_data()
        """
        self.queue_.insert(0, item)
        self.size_ += 1

    def pop_back(self):
        self.size_ -= 1
        return self.queue_.pop()

    def pop_front(self):
        self.size_ -= 1
        return self.queue_.pop(0)

    def insert(self, index=-1, item=None):
        """
        item: 为Internal_data()
        """
        if index < -self.size_:
            self.queue_.insert(0, item)
        elif index > self.size_:
            self.queue_.append(item)
        else:
            self.queue_.insert(index, item)
        self.size_ += 1

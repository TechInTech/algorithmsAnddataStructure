# -*- coding:utf-8 -*-

from node import Node


class LinkedQueue(object):
    def __init__(self):
        self.front_ = None
        self.rear_ = None
        self.size_ = 0

    def isEmpty(self):
        if self.__len__() == 0:
            return True
        else:
            False

    def __len__(self):
        return self.size_

    def __iter__(self):
        if self.isEmpty():
            raise KeyError('The queue is empty.')
        templist = list()
        while self.front_.next is not None:
            templist.append(self.front_.data)
        templist.append(self.front_.data)
        return iter(templist)

    def add(self, item):
        newnode = Node(item)
        if self.isEmpty():
            self.front_ = newnode
        else:
            self.rear_.next = newnode
        self.rear_ = newnode
        self.size_ += 1

    def peek(self):
        if self.isEmpty():
            raise KeyError('The queue is empty.')
        item = self.front_.data
        return item

    def pop(self):
        if self.isEmpty():
            raise KeyError('The queue is empty.')
        item = self.front_.data
        self.front_ = self.front_.next
        self.size_ -= 1
        return item

# -*- coding:utf-8 -*-

from node import Node

class Stack(object):
    def __init__(self):
        self.items = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def clear(self):
        self.size = 0
        self.items = None

    def peek(self):
        if self.isEmpty():
            raise KeyError('The stack is empty.')
        return self.items.data

    def push(self, item):
        self.items = Node(item, self.items)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError('The stack is empty.')
        value = self.items.data
        self.items = self.items.next
        self.size -= 1
        return value

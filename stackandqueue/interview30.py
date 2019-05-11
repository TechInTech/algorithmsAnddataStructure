# -*- coding:utf-8 -*-

"""包含min函数的栈
"""

class Solution_30(object):
    def __init__(self):
        self.cursor = -1
        self.m_data = []
        self.m_min = []

    def push(self, value):
        if self.cursor == -1:
            self.m_data.append(value)
            self.m_min.append(value)
        else:
            if self.m_min[self.cursor] <= value:
                self.m_min.append(self.m_min[self.cursor])
            else:
                self.m_min.append(value)
            self.m_data.append(value)
        self.cursor += 1

    def pop(self):
        if self.cursor == -1:
            return None
        else:
            del self.m_min[self.cursor]
            value = self.m_data[self.cursor]
            del self.m_data[self.cursor]
            self.cursor -= 1
            return value

    def top(self):
        if self.cursor == -1:
            return None
        else:
            return self.m_data[self.cursor]

    def min(self):
        if self.cursor == -1:
            return None
        else:
            return self.m_data[self.cursor]

from node import Node
from stack import Stack

class Solution_30b(object):
    def __init__(self):
        self.main_stack = Stack()
        self.min_stack = Stack()

    def push(self, value):
        if self.main_stack.isEmpty():
            self.main_stack.push(value)
            self.min_stack.push(value)
        else:
            if value < self.min_stack.peek():
                self.min_stack.push(value)
            else:
                self.min_stack.push(self.min_stack.peek())
            self.main_stack.push(value)

    def pop(self):
        if self.main_stack.isEmpty():
            raise KeyError('The stack is empty.')
        else:
            self.min_stack.delete()
            return self.main_stack.pop()

    def top(self):
        return self.main_stack.peek()

    def min(self):
        if self.main_stack.isEmpty():
            raise KeyError('The stack is empty.')
        return self.min_stack.peek()

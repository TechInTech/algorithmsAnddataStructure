# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, value=None, next=None):
        self.data = value
        self.next = next


class LinkedNode(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return False
        else:
            return True

    def __len__(self):
        return self.size

    def add(self, node):
        if self.isEmpty():
            self.head = node
            self.size += 1
        else:
            front = self.head
            while front.next is not None:
                front = front.next
            front.next = node
            self.size += 1

    def __str__(self):
        result = ''
        front = self.head
        while front.next is not None:
            result += str(front.data) + ', '
            front = front.next
        result += str(front.data) + ','
        return result
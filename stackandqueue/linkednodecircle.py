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
            return True
        else:
            return False

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

    def create_circle_node(self, startpoint):
        if startpoint <= 0 or startpoint >= self.size:
            raise KeyError(
                'The enter of circle node is not in the range from 1 to %d!' % startpoint)

        self.cusor = 0
        head = self.head
        while head.next is not None:
            self.cusor += 1
            if self.cusor == startpoint:
                node = head
            head = head.next
        head.next = node

    def __str__(self):
        result = ''
        front = self.head
        while front.next is not None:
            result += str(front.data) + ', '
            front = front.next
        result += str(front.data) + ','
        return result

    def listofnode(self):
        nodelist = list()
        front = self.head
        while front.next is not None:
            nodelist.append(front)
            front = front.next
        nodelist.append(front)
        return nodelist

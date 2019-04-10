# -*- coding:utf-8 -*-

import copy
from stack import Stack
from node import Node


class LinkedQueue(object):
    def __init__(self):
        self.front_ = Stack()
        self.rear_ = Stack()

    def isEmpty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def __len__(self):
        return self.front_.size + self.rear_.size

    def appendTail(self, item):
        self.rear_.push(item)

    def deleteHead(self):
        if self.isEmpty():
            raise KeyError('The queue is empty.')
        elif self.front_.size == 0 and self.rear_.size != 0:
            while self.rear_.items.next is not None:
                self.front_.push(self.rear_.pop())
            self.front_.push(self.rear_.pop())
            value = self.front_.pop()
            return value
        else:
            value = self.front_.pop()
            return value

    # def appendTail(self, item):
    #     self.rear_.push(item)
    #     self.size_ += 1
    #
    #     self.front_.clear()
    #     i = self.__len__()
    #     tempnode = copy.copy(self.rear_)
    #     while i > 0:
    #         self.front_.push(tempnode.pop())
    #         i -= 1
    #
    # def deleteHead(self):
    #     if self.front_.isEmpty():
    #         raise KeyError('The queue is empty.')
    #     self.front_.pop()
    #     self.size_ -= 1
    #
    #     self.rear_.clear()
    #     i = self.__len__()
    #     tempnode = copy.copy(self.front_)
    #     while i > 0:
    #         self.rear_.push(tempnode.pop())
    #         i -= 1

    def __iter__(self):
        def visitnode1(node):
            if node is not None:
                tempList.append(node.data)
                visitnode1(node.next)

        def visitnode2(node):
            if node is not None:
                visitnode2(node.next)
                tempList.append(node.data)

        tempList = list()
        visitnode1(self.front_.items)
        visitnode2(self.rear_.items)
        return iter(tempList)

def main():

    newqueue = LinkedQueue()
    print('************** We will Create a new queue! **************')
    queuelist = []
    while True:
        item = input('Please input the items of queeu:')
        if item == '':
            break
        queuelist.append(item)
        print('The items of the queue is:',queuelist)
        newqueue.appendTail(item)
    while True:
        delnode = newqueue.deleteHead()
        print('The deleted node in queue is ' + delnode)

    exit()

    queuelist.remove(delnode)

    for item in newqueue:
        print(item, end=',')

    print('\n')

    while True:
        item = input('Please input the items of queeu:')
        if item == '':
            break
        queuelist.append(item)
        print('The items of the queue is:',queuelist)
        newqueue.appendTail(item)


    delnode = newqueue.deleteHead()
    print('The deleted node in queue is ' + delnode)
    queuelist.remove(delnode)

    for item in newqueue:
        print(item, end=',')

if __name__ == '__main__':
    main()

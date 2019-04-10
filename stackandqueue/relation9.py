# -*- coding:utf-8 -*-

import copy
from linkedqueue import LinkedQueue

class Stack(object):
    def __init__(self):
        self.stack1 = LinkedQueue()
        self.stack2 = LinkedQueue()

    def isEmpty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def __len__(self):
        if self.stack1.size_ == 0:
            return self.stack2.size_
        else:
            return self.stack1.size_

    def peek(self):
        if self.isEmpty():
            raise KeyError('The stack is empty.')
        elif not self.stack1.isEmpty():
            item = self.stack1.peek()
            return item
        else:
            item = self.stack2.peek()
            return item

    def push(self, item):
        if self.isEmpty() or (not self.stack1.isEmpty() and self.stack2.isEmpty()):
            self.stack1.add(item)
        else:
            self.stack2.add(item)

    def pop(self):
        if self.isEmpty():
            raise KeyError('The stack is empty.')
        if not self.stack1.isEmpty():
            while self.stack1.front_.next is not None:
                self.stack2.add(self.stack1.pop())
            item = self.stack1.pop()
            return item
        else:
            while self.stack2.front_.next is not None:
                self.stack1.add(self.stack2.pop())
            item = self.stack2.pop()
            return item

    # def __iter__(self):
    #     def travser_stack_recursive(sta, templist):
    #         if sta.front_.next is not None:
    #             templist = travser_stack_recursive(sta.front_.next, templist)
    #         templist.append(sta.front_.data)
    #         return templist
    #
    #     templist = list()
    #     if self.isEmpty():
    #         raise KeyError('The stack is empty.')
    #
    #     if not self.stack1.isEmpty():
    #         travser_stack_recursive(self.stack1, templist)
    #         return iter(templist)
    #     else:
    #         travser_stack_recursive(self.stack2, templist)
    #         return iter(templist)

    def __iter__(self):
        if self.isEmpty():
            raise KeyError('The stack is empty.')
        templist = list()
        if not self.stack1.isEmpty():
            tempstack = copy.copy(self.stack1)
            while tempstack.front_.next is not None:
                templist.append(tempstack.pop())
            templist.append(tempstack.pop())
            templist.reverse()  # ******
            return iter(templist)
        else:
            tempstack = copy.copy(self.stack2)
            while tempstack.front_.next is not None:
                templist.append(tempstack.pop())
            templist.append(tempstack.pop()).reverse()
            templist.reverse()  # ******
            return iter(templist)

def main():
    newstack = Stack()
    print('************** We will Create a new stack! **************')
    stacklist = []
    while True:
        item = input('Please input the items of stack:')
        if item == '':
            break
        stacklist.append(item)
        print('The items of the stack is:',stacklist)
        newstack.push(item)
    for i in newstack:
        print(i)
    while True:
        delnode = newstack.pop()
        print('The deleted node in stack is ' + delnode)

if __name__ == '__main__':
    main()

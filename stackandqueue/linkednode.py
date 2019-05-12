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

    def add(self, value):
        node = Node(value)
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

    def listofnode(self):
        nodelist = list()
        front = self.head
        while front.next is not None:
            nodelist.append(front)
            front = front.next
        nodelist.append(front)
        return nodelist

def main():
    ls = ['A', 'B', 'C', 'D', 'E']
    complnodes = LinkedNode()
    for item in ls:
        complnodes.add(item)

    head = complnodes.head
    count = 0
    while head.next is not None:
        count += 1
        print(head.data)
        head = head.next
    print(count)
    print(complnodes.__str__())

if __name__ == '__main__':
    main()

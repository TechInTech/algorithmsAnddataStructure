# -*- utf:-8 -*-


class Node(object):
    def __init__(self, value=None, next=None):
        self.data = value
        self.next = next


class Stack(object):
    def __init__(self):
        self.item = list()
        self.size = 0

    def push(self, value):
        self.item.append(value)
        self.size += 1

    def pop(self):
        item = self.item[self.size - 1]
        self.size -= 1
        return item


class LinkedNode(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, node):
        if self.head is None:
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

    def reverse_output(self):
        otstack = Stack()
        front = self.head
        while front.next is not None:
            otstack.push(front.data)
            front = front.next
        otstack.push(front.data)
        length = otstack.size
        for i in range(length):
            print(otstack.pop(), end=', ')

    # def reverse_output_recursive(self, head = self.head):
    #     # head = self.head
    #     if head is not None:
    #         if head.next is not None:
    #             # self.head = head.next
    #             self.reverse_output_recursive(head.next)
    #         else:
    #             print(head.data)


def main():
    ln = LinkedNode()
    strings = 'abcdefghijklmnopqrstuvwxyz'
    strings = ' '
    for i in strings:
        ln.add(Node(i))
    print(ln)
    ln.reverse_output()
    # ln.reverse_output_recursive()


if __name__ == '__main__':
    main()

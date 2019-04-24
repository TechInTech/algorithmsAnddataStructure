import numpy as np
from linkednode import LinkedNode, Node


class Solution_24(object):

    def __init__(self):
        self.previous = None
        self.current = None
        self.later = None

    def reverse_linkednode(self, head):
        self.current = head
        while self.current is not None:
            nextnode = self.current.next

            if nextnode is None:
                self.later = self.current

            self.current.next = self.previous

            self.previous = self.current
            self.current = nextnode

        return self.later


def main():
    linknode = LinkedNode()
    value_list = np.random.randint(1, 7, 6).tolist()

    for i in value_list:
        node = Node(i)
        linknode.add(node)

    print('The LinkedNode is: ' + linknode.__str__())

    reverselinkednode = Solution_24()
    reversenode = reverselinkednode.reverse_linkednode(linknode.head)

    reversehead = reversenode

    while reversehead.next is not None:
        print(reversehead.data, end=', ')
        reversehead = reversehead.next
    print(reversehead.data, end=', ')


if __name__ == '__main__':
    main()

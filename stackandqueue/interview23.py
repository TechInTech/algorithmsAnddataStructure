import numpy as np
from linkednodecircle import LinkedNode, Node


class Solution_23(object):

    def __init__(self):
        self.point1 = None
        self.point2 = None

    def meeting_node(self, head):
        if head is None:
            raise KeyError('The node is empty!')

        self.point1 = head.next
        if self.point1 is None:
            return None

        self.point2 = self.point1.next
        while self.point2 is not None and self.point1 is not None:
            if self.point1 == self.point2:
                return self.point2

            self.point1 = self.point1.next
            self.point2 = self.point2.next

            if self.point2 is not None:
                self.point2 = self.point2.next

        return None

    def entry_node_of_loop(self, head):
        meetingnode = self.meeting_node(head)
        if meetingnode is None:
            return None

        nodesinloop = 1
        entrynode1 = meetingnode
        while entrynode1.next is not meetingnode:
            entrynode1 = entrynode1.next
            nodesinloop += 1

        entrynode1 = head
        for i in range(nodesinloop):
            entrynode1 = entrynode1.next

        entrynode2 = head
        while entrynode1 is not entrynode2:
            entrynode1 = entrynode1.next
            entrynode2 = entrynode2.next

        return entrynode1


def main():
    linknode = LinkedNode()
    value_list = np.random.randint(1, 7, 6).tolist()

    for i in value_list:
        node = Node(i)
        linknode.add(node)

    print('The LinkedNode is: ' + linknode.__str__())

    k = np.random.randint(1, 5)
    print('The node %d is the enter of circle linked node.' % k)

    linknode.create_circle_node(k)

    begin = 0
    head = linknode.head
    while begin < 15:
        begin += 1
        value = head.data
        head = head.next
        if begin == k:
            print('****The enter Node****')
        print('%2d: %d' % (begin, value))

    searchentry = Solution_23()
    entrynode = searchentry.entry_node_of_loop(linknode.head)

    if entrynode is None:
        print('The linked node list has not loop!')
    else:
        print('The entry node\'s value is:%d' % entrynode.data)


if __name__ == '__main__':
    main()

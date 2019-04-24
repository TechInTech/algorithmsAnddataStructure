import numpy as np
from linkednode import LinkedNode, Node

class Solution_22(object):

    def __init__(self):
        self.point1 = 1
        self.point2 = 1

    def output_k_node_in_linkednode(self, linknode, k):
        if k > linknode.__len__():
            raise KeyError('The k is out of the index of LinkedNode !')
        elif linknode.isEmpty():
            raise KeyError('The LinkedNode is empty!')
        elif k == 0:
            raise KeyError('The k is less than 1!')

        head1 = linknode.head
        while self.point2 < k:
            head1 = head1.next
            self.point2 += 1
        head2 = linknode.head

        while head1.next is not None:
            head1 = head1.next
            head2 = head2.next

        value = head2.data

        print('The value to be output in LinkedNode is: ' + str(value))


def main():
    linknode = LinkedNode()
    value_list = np.random.randint(1,7,6).tolist()

    for i in value_list:
        node = Node(i)
        linknode.add(node)

    print('The LinkedNode is: ' + linknode.__str__())

    k = value_list[np.random.randint(1,6)]
    print('The number to be deleted is: ' + str(k))

    outputnode = Solution_22()
    outputnode.output_k_node_in_linkednode(linknode, k)


if __name__ == '__main__':
    main()

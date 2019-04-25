import numpy as np
from linkednode  import LinkedNode, Node

class Solution_25(object):
    # def __init__(self):
    #     # self.linknode = LinkedNode()
    #     self.listnode = None

    def merge(self, head1, head2):
        if not (head1 or head2):
            return None
        elif head1 is None:
            return head2
        elif head2 is None:
            return head1


        if head1.data < head2.data:
            mergenode = head1
            mergenode.next = self.merge(head1.next, head2)
        else:
            mergenode = head2
            mergenode.next = self.merge(head1, head2.next)

        return mergenode


def main():
    linknode1 = LinkedNode()
    value_list = np.sort(np.random.randint(1, 7, 6))

    for i in value_list:
        node = Node(i)
        linknode1.add(node)

    print('The LinkedNode1 is: ' + linknode1.__str__())

    linknode2 = LinkedNode()
    value_list = np.sort(np.random.randint(1, 10, 6))

    for i in value_list:
        node = Node(i)
        linknode2.add(node)

    print('The LinkedNode2 is: ' + linknode2.__str__())

    linknode3 = Solution_25()

    result = linknode3.merge(linknode1.head, linknode2.head)

    print('After merge the two LinkedNode:')
    while result.next is not None:
        print(result.data, end=', ')
        result = result.next
    print(result.data, end=', ')



if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-

"""复杂链表的复制
"""
from complexlistnode import ComplexListNode
from complexlinkednode import ComplexLinkedNode

class Solution_35(object):

    # def __init__(self, phead=None):
    #     self.phead = phead

    def clone_nodes(self, phead):
        pnode = phead

        while pnode:
            pcloned = ComplexListNode()
            pcloned.data_ = pnode.data_
            pcloned.next_ = pnode.next_

            pnode.next_ = pcloned
            pnode = pcloned.next_

        return phead

    def connect_sibling_nodes(self, phead):
        pnode = phead
        while pnode:
            pcloned = pnode.next_
            if pnode.sibling_:
                pcloned.sibling_ = pnode.sibling_.next_
            pnode = pcloned.next_
        return phead

    def reconnect_node(self, phead):
        pnode = phead
        pclonedhead = None
        pclonednode = None

        if pnode:
            pclonedhead = pclonednode = pnode.next_
            pnode.next_ = pclonednode.next_
            pnode = pnode.next_

        while pnode:
            pclonednode.next_ = pnode.next_
            pclonednode = pclonednode.next_
            pnode.next_ = pclonednode.next_
            pnode = pnode.next_

        return pclonedhead

    def clone(self, phead):
        p1 = self.clone_nodes(phead)
        p2 = self.connect_sibling_nodes(p1)
        return self.reconnect_node(p2)


def main():
    head = ComplexLinkedNode().example()

    s35 = Solution_35()
    clonednodes = s35.clone(head)

    node = clonednodes
    # print()
    while node.next_:
        # print(node.data_)
        print(node.data_, '-->', node.sibling_.data_ if node.sibling_ else None)
        node = node.next_
    # print(node.data_)
    print(node.data_, '-->', node.sibling_.data_ if node.sibling_ else None)


if __name__ == '__main__':
    main()

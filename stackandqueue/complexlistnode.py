# -*- coding:utf-8 -*-

"""复杂链表节点的定义
"""
class ComplexListNode(object):

    def __init__(self, data=None, next=None, sibling=None):
        """
        data: the value of node(constant)
        next: the pointer point to next node
        sibling: the pointer point to any node of linked node
        """
        self.data_ = data
        self.next_ = next
        self.sibling_ = sibling

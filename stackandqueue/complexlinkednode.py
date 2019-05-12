# -*- coding:utf-8 -*-

from complexlistnode import ComplexListNode

class ComplexLinkedNode(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def add(self, value=None):
        node = ComplexListNode(data=value)
        if self.isEmpty():
            self.head = node
            self.size += 1
        else:
            front = self.head
            while front.next_ is not None:
                front = front.next_
            front.next_ = node
            self.size += 1

    def __str__(self):
        result = ''
        front = self.head
        while front.next_ is not None:
            result += str(front.data_) + ', '
            front = front.next_
        result += str(front.data_)
        return result

    def listofnode(self):
        nodelist = list()
        front = self.head
        while front.next_ is not None:
            nodelist.append(front)
            front = front.next_
        nodelist.append(front)
        return nodelist

    def connet_node(self, fromnode=None, tonode=None):
        fromnode.sibling_ = tonode
        # return self.head

    def example(self):
        ls = ['A', 'B', 'C', 'D', 'E']
        for item in ls:
            self.add(value=item)
        node_ls = self.listofnode()
        index_ls = [(0, 2), (1, 4), (3, 1)]
        for i_tup in index_ls:
            self.connet_node(node_ls[i_tup[0]], node_ls[i_tup[1]])
        return self.head


def main():
    ls = ['A', 'B', 'C', 'D', 'E']
    complnodes = ComplexLinkedNode()
    for item in ls:
        complnodes.add(value=item)

    print(complnodes.__str__())

    node_ls = complnodes.listofnode()
    index_ls = [(0, 2), (1, 4), (3, 1)]
    for i_tup in index_ls:
        complnodes.connet_node(node_ls[i_tup[0]], node_ls[i_tup[1]])
    nodes_ls = complnodes.listofnode()
    for node in nodes_ls:
        print(node.data_, '-->', node.sibling_.data_ if node.sibling_ else None)

if __name__ == '__main__':
    main()

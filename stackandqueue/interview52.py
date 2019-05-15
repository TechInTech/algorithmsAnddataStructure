# -*- coding:utf-8 -*-
"""两个链表的第一个公共节点
"""

class Solution_52(object):
    def find_first_common_node(self, head1, head2):
        """
        head1: 链表1的头结点
        head2: 链表2的头结点
        """
        length1 = self.get_length(head1)
        length2 = self.get_length(head2)

        if length1 >= length2:
            headlong = head1
            headshort = head2
            length_between = length1 - length2
        else:
            headlong = head2
            headshort = head1
            length_between = length2 - length1

        for i in range(length_between):
            headlong = headlong.next

        while headlong and headshort and headlong.data != headshort.data:
            headlong = headlong.next
            headshort = headshort.next

        first_common_node = headlong
        return first_common_node

    def get_length(self, head):
        length = 0
        phead = head
        while phead:
            phead = phead.next
            length += 1
        return length

from linkednode import LinkedNode

def main():
    ls1 = [1, 2, 3, 4, 5, 6, 7, 8]
    ls2 = [0, 5, 6, 7, 8]

    # 创建链表
    link1 = LinkedNode()
    link2 = LinkedNode()

    for i in ls1:
        link1.add(i)

    for j in ls2:
        link2.add(j)
    # print(link2.listofnode())

    commom_node = Solution_52().find_first_common_node(link1.head, link2.head)
    print('Two list node\'s commom node are %d.'%commom_node.data)

    # commom_node = Solution_52().get_length(link2.head)
    # print('Two LinkedNode\'s commom node are %d'%commom_node)


if __name__ == '__main__':
    main()

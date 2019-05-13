# -*- coding:utf-8 -*-
"""二叉搜索树与双向链表
"""

from generate_tree import Generate_tree

class Solution_36(object):

    def convert(self, tree_root):
        plast = None
        plast = self.convert_node(tree_root, plast)

        phead = plast
        while phead and phead.left_:
            phead = phead.left_

        return phead

    def convert_node(self, pnode, plast):
        if pnode is None:
            return

        pcurrent = pnode

        if pcurrent.left_:
            plast = self.convert_node(pcurrent.left_, plast)

        pcurrent.left_ = plast
        if plast:
            plast.right_ = pcurrent

        plast = pcurrent

        if pcurrent.right_:
            plast = self.convert_node(pcurrent.right_, plast)
        return plast

def main():

    tree_root = Generate_tree().create_tree()

    doublelink = Solution_36().convert(tree_root)
    # print(doublelink)

    while doublelink:
        print(doublelink.data_)
        doublelink = doublelink.right_

if __name__ == '__main__':
    main()

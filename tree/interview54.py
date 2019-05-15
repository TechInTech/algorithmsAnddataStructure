# -*- coding:utf-8 -*-
"""二叉搜索树的第K大节点
"""
from generate_tree import Generate_tree
from binarytree import BinaryTreeNode

class Solution_54(object):
    def __init__(self, k=None):
        self.k = k

    def kth_node(self, tree_root):
        if tree_root is None or self.k == 0:
            return None
        return self.kth_node_core(tree_root)

    def kth_node_core(self, tree_root):
        target = None
        if tree_root.left_:
            target = self.kth_node_core(tree_root.left_)

        if target is None:
            if self.k == 1:
                target = tree_root
            self.k -= 1

        if target is None and tree_root.right_:
            target = self.kth_node_core(tree_root.right_)
        return target


def main():
    tree = Generate_tree()
    tree_root = tree.create_tree()
    tree.print_structure()

    k = 4
    result = Solution_54(k).kth_node(tree_root)
    print('The %dth largest node is %d'%(k, result.data_))


if __name__ == '__main__':
    main()

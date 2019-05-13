# -*- coding:utf-8 -*-
"""序列化二叉树
"""
from binarytree import BinaryTreeNode
from generate_tree import Generate_tree

class Solution_37(object):

    def __init__(self):
        self.strings = ''

    def serialize(self, tree_root):
        if tree_root is None:
            self.strings += '$,'
            return

        self.strings += str(tree_root.data_) + ','
        self.serialize(tree_root.left_)
        self.serialize(tree_root.right_)


    def deserialize(self, root):
        str_ls = self.strings.split(',')
        return self.deserializetree(str_ls)

    def deserializetree(self, ls):
        if len(ls) <= 0:
            return None
        val = ls.pop(0)
        root = None
        if val != '$':
            root = BinaryTreeNode(int(val))
            root.left_ = self.deserializetree(ls)
            root.right_ = self.deserializetree(ls)
        return root

def main():
    g_tree = Generate_tree()

    tree_root = g_tree.create_tree()

    g_tree.print_structure()

    s37 = Solution_37()
    s37.serialize(tree_root)

    print(s37.strings)

    tree = s37.deserialize(s37.strings)

    def recurse(node, level):
            s = ''
            if node is not None:
                s += recurse(node.right_, level + 1)
                s += '| ' * level
                s += str(node.data_) + ' \n'
                s += recurse(node.left_, level + 1)
            return s
    print('Tree structure:')
    print(recurse(tree, 0))

if __name__ == '__main__':
    main()

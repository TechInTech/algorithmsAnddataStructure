# -*- coding:utf-8 -*-

from binarytree import BinaryTreeNode
from tree import Tree


class Solution_26(object):

    def has_subtree(self, tree1, tree2):
        result = False

        if tree1 is not None and tree2 is not None:
            if self.isequal(tree1.data_, tree2.data_):
                result = self.tree1_has_tree2(tree1, tree2)
            if not result:
                result = self.has_subtree(tree1.left_, tree2)
            if not result:
                result = self.has_subtree(tree1.right_, tree2)
        return result

    def tree1_has_tree2(self, tree1, tree2):
        if tree2 is None:
            return True

        if tree1 is None:
            return True

        if not self.isequal(tree1.data_, tree2.data_):
            return False

        return self.tree1_has_tree2(tree1.left_, tree2.left_) and self.tree1_has_tree2(tree1.right_, tree2.right_)

    def isequal(self, num1, num2):
        if (num1 - num2 > -0.0000001) and (num1 - num2 < 0.0000001):
        # if (num1 == num2):
            return True
        else:
            return False


def main():
    # 由前序遍历和中序遍历产生树
    preo = [1, 2, 4, 7, 3, 5, 6, 8]
    ino = [4, 7, 2, 1, 5, 3, 8, 6]
    length = len(preo)
    cls_Tree = Tree()
    cls_Tree.gene_tree(preo, ino, length)
    main_tree = cls_Tree.get_tree()
    cls_Tree.travel_tree(main_tree)

    print('\n\n****************subtree*******************\n')

    # 子树
    preo = [3, 5, 6]
    ino = [5, 3, 6]
    length = len(preo)
    cls_sub_Tree = Tree()
    cls_sub_Tree.gene_tree(preo, ino, length)
    sub_tree = cls_sub_Tree.get_tree()
    cls_sub_Tree.travel_tree(sub_tree)

    decide = Solution_26()
    result = decide.has_subtree(main_tree, sub_tree)
    print('\n')
    if result:
        print('The subtree belongs to tree!')
    else:
        print('The subtree do not belong to tree!')


if __name__ == '__main__':
    main()

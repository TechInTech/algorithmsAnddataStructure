# -*- coding:utf-8 -*-

"""二叉树中和为某一直的路径
"""
import copy
from generate_tree import Generate_tree

class Solution_34(object):

    def __init__(self):
        self.result = []
        self.stack = []
        self.sum = 0

    def findpath(self, tree_root, exception):
        if tree_root is None:
            return None
        self.find(tree_root, exception)
        return self.result

    def find(self, tree_root, exception):
        self.stack.append(tree_root.data_)
        self.sum += tree_root.data_

        if tree_root.left_:
            self.find(tree_root.left_, exception)
        if tree_root.right_:
            self.find(tree_root.right_, exception)
        if (not tree_root.left_) or (not tree_root.right_):
            if self.sum == exception:
                self.result.append(copy.deepcopy(self.stack))
        self.sum -= tree_root.data_
        self.stack.pop()


def main():
    tree = Generate_tree()
    tree_root = tree.create_tree()

    tree.print_structure()

    s34 = Solution_34()
    excep = 22
    result = s34.findpath(tree_root, excep)
    if result:
        print('The paths which sum is %d are:' % excep)
        print(result)
    else:
        print('There do not exist a path.')

if __name__ == '__main__':
    main()

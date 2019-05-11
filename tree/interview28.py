# -*- coding: utf-8 -*-

from generate_tree import Generate_tree

class Solution_28(object):
    def is_symmetrical(self, binarytree):
        return self.is_symmetrical_1(binarytree, binarytree)

    def is_symmetrical_1(self, binarytree1, binarytree2):
        if binarytree1 is None and binarytree2 is None:
            return True
        if binarytree1 is None or binarytree2 is None:
            return False
        if binarytree1.data_ != binarytree2.data_:
            return False
        return self.is_symmetrical_1(binarytree1.left_, binarytree2.right_) and \
        self.is_symmetrical_1(binarytree1.right_, binarytree2.left_)


def main():
    tree_root = Generate_tree().create_tree()

    s28 = Solution_28()
    result = s28.is_symmetrical(tree_root)
    if result:
        print('The binarytree is symmetrical.')
    else:
        print('The binarytree is not symmetrical.')


if __name__ == '__main__':
    main()

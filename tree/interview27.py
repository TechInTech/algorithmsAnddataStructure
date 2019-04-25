# -*- coding:utf-8 -*-
from tree import Tree


class Solution_27(object):

    def mirror_recursive(self, binarytree):
        if binarytree is None:
            return

        if binarytree.left_ is None and binarytree.right_ is None:
            return

        binarytree.left_, binarytree.right_ = binarytree.right_, binarytree.left_

        if binarytree.left_:
            self.mirror_recursive(binarytree.left_)

        if binarytree.right_:
            self.mirror_recursive(binarytree.right_)

        return binarytree


def main():
    preo = [1, 2, 4, 7, 3, 5, 6, 8]
    ino = [4, 7, 2, 1, 5, 3, 8, 6]
    length = len(preo)
    cls_Tree = Tree()
    cls_Tree.gene_tree(preo, ino, length)
    main_tree = cls_Tree.get_tree()
    # cls_Tree.travel_tree(main_tree)
    print(cls_Tree.structure_of_tree(main_tree))


    print('\n*****After mirror *****\n')
    tobedelt_tree = Solution_27()
    mirror_tree = tobedelt_tree.mirror_recursive(main_tree)
    # cls_Tree.travel_tree(mirror_tree)
    print(cls_Tree.structure_of_tree(mirror_tree))


if __name__ == '__main__':
    main()

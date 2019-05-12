# -*- coding:utf-8 -*-

from binarytree import BinaryTreeNode


class Tree(object):
    def __init__(self):
        self.root = None

    def gene_tree(self, preorder, inorder, length):
        """Generate the tree by the preorder sequence, inorder sequence and the length of sequence.
        """
        if len(inorder) == 0 or length == 0:
            return -1
        fro = 0
        rear = length - 1
        self.root = self.constructtree(preorder, inorder, fro, rear, fro, rear)

    def get_tree(self):
        return self.root

    def constructtree(self, preorder, inorder, k1, Lk1, k2, Lk2):
        rootval = preorder[k1]
        root = BinaryTreeNode(rootval)

        if k1 == Lk1:
            if k2 == Lk2 and preorder[k1] == inorder[k2]:
                return root
            else:
                raise ValueError

        rootino = k2
        while rootino <= Lk2 and inorder[rootino] != rootval:
            rootino += 1

        if rootino == Lk2 and inorder[rootino] != rootval:
            raise ValueError

        leftlength = rootino - k2
        leftpreo = k1 + leftlength

        if leftlength > 0:
            root.left_ = self.constructtree(
                preorder, inorder, k1 + 1, leftpreo, k2, rootino - 1)

        if leftlength < (Lk1 - k1):
            root.right_ = self.constructtree(
                preorder, inorder, leftpreo + 1, Lk1, rootino + 1, Lk2)
        return root

    def travel_tree(self, tree):
        print(tree.data_)    # preorder travel
        if tree.left_ is not None:
            self.travel_tree(tree.left_)
        # print(tree.data_)    # inorder travel
        if tree.right_ is not None:
            self.travel_tree(tree.right_)
        # print(tree.data_)    # postorder travel
        return

    def structure_of_tree(self, tree):

        def recurse(node, level):
            s = ''
            if node is not None:
                s += recurse(node.right_, level + 1)
                s += '| ' * level
                s += str(node.data_) + '\n'
                s += recurse(node.left_, level + 1)
            return s

        print('Tree structure:')
        print(recurse(tree, 0))

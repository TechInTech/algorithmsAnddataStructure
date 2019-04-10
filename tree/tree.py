# -*- coding:utf-8 -*-


class BinaryTreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.data_ = value
        self.left_ = left
        self.right_ = right


class Tree(object):
    def __init__(self):
        pass

    def gene_tree(self, preorder, inorder, length):
        """Generate the tree by the preorder sequence, inorder sequence and the length of sequence.
        """
        if preorder == [] or inorder == [] or length <= 0:
            return -1
        fro = 0
        rear = length - 1
        return self.constructtree(preorder, inorder, fro, rear, fro, rear)


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
        # print(tree.data_)    # preorder travel
        if tree.left_ is not None:
            self.travel_tree(tree.left_)
        print(tree.data_)    # inorder travel
        if tree.right_ is not None:
            self.travel_tree(tree.right_)
        # print(tree.data_)    # postorder travel
        return

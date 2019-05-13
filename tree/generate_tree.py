# -*- coding:utf-*-
from tree import Tree

class Generate_tree(object):

    def __init__(self):
        # print('Please input the preorder traverse of tree:')
        # self.preo_ls = self.get_sequence()
        self.preo_ls = [10, 6, 4, 8, 14, 12,  16]
        # print('The preorder is:', self.preo_ls)

        # print('Please input the inorder traverse of tree:')
        # self.ino_ls = self.get_sequence()
        self.ino_ls = [4, 6, 8, 10, 12, 14, 16]
        # print('The inorder is:', self.ino_ls)

        self.length = len(self.preo_ls)

    def get_sequence(self):
        sequ_ls = []
        while True:
            string = input()
            if string is '':
                break
            sequ_ls.append(int(string))
        return sequ_ls

    def create_tree(self):
        self.tree = Tree()
        self.tree.gene_tree(self.preo_ls, self.ino_ls, self.length)
        return self.tree.get_tree()

    def travel(self):
        self.tree.travel_tree(self.create_tree())

    def print_structure(self):
        self.tree.structure_of_tree(self.create_tree())

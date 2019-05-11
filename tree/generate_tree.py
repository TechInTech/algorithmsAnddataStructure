# -*- coding:utf-*-
from tree import Tree

class Generate_tree(object):
    def __init__(self):
        print('Please input the preorder traverse of tree:')
        self.preo_ls = self.get_sequence()
        print('The preorder is:', self.preo_ls)

        print('Please input the inorder traverse of tree:')
        self.ino_ls = self.get_sequence()
        print('The preorder is:', self.ino_ls)

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
        self.tree.travel_tree(self.tree.root)

    def print_structure(self):
        self.tree.structure_of_tree(self.tree.root)

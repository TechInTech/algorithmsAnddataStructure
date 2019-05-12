# -*- coding:utf-8 -*-
from linkedqueue import LinkedQueue
from generate_tree import Generate_tree

class Solution_32b(object):

    def __init__(self):
        self.queue = LinkedQueue()

    def print_tree(self, treeroot):
        if treeroot is None:
            return

        self.queue.add(treeroot)

        nextlevel, tobeprinted = 0, 1

        print('Print the tree structure by level.')
        while not self.queue.isEmpty():
            pnode = self.queue.peek()
            print('%d'% pnode.data_, end=' | ')
            if pnode.left_ is not None:
                self.queue.add(pnode.left_)
                nextlevel += 1
            if pnode.right_ is not None:
                self.queue.add(pnode.right_)
                nextlevel += 1
            self.queue.pop()
            tobeprinted -= 1
            if tobeprinted == 0:
                print('\n')
                tobeprinted = nextlevel
                nextlevel = 0

def main():
    tree = Generate_tree()
    tree_root = tree.create_tree()

    tree.print_structure()

    s32b = Solution_32b()
    s32b.print_tree(tree_root)


if __name__ == '__main__':
    main()

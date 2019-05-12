# -*- coding:utf-8 -*-
from stack import Stack
from generate_tree import Generate_tree

class Solution_32c(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def print_tree(self, treeroot):
        if treeroot is None:
            return None

        stack_ls = [self.stack1, self.stack2]
        current, next = 0, 1

        stack_ls[current].push(treeroot)

        print('之字形打印树结构:')
        while not stack_ls[0].isEmpty() or not stack_ls[1].isEmpty():
            pnode = stack_ls[current].peek()
            stack_ls[current].pop()

            print('%d'% pnode.data_, end=' | ')

            if current == 0:
                if pnode.left_ is not None:
                    stack_ls[next].push(pnode.left_)

                if pnode.right_ is not None:
                    stack_ls[next].push(pnode.right_)
            else:
                if pnode.right_ is not None:
                    stack_ls[next].push(pnode.right_)
                if pnode.left_ is not None:
                    stack_ls[next].push(pnode.left_)
            if stack_ls[current].isEmpty():
                print('\n')
                current = 1 - current
                next = 1 - next

def main():
    tree = Generate_tree()
    tree_root = tree.create_tree()

    tree.print_structure()

    s32c = Solution_32c()
    s32c.print_tree(tree_root)


if __name__ == '__main__':
    main()

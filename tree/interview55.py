# -*- coding:utf-8 -*-
"""二叉树的深度
"""

class Solution_55(object):
    def tree_depth(self, tree_root):
        if not tree_root:
            return 0

        left = self.tree_depth(tree_root.left_)
        right = self.tree_depth(tree_root.right_)

        return (left + 1) if left > right else (right + 1)

from generate_tree import Generate_tree

def main():
    tree = Generate_tree()
    tree_root = tree.create_tree()
    tree.print_structure()

    depth = Solution_55().tree_depth(tree_root)
    print('The depth of tree is %d.'%depth)


if __name__ == '__main__':
    main()

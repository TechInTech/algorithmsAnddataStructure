# -*- coding:utf-8 -*-
"""平衡二叉树
"""

class Solution_55b(object):

    # ********************* method 1 **************************
    def is_balance(self, tree_root):
        if not tree_root:
            # self.depth = 0
            return True

        left, right = self.tree_depth(tree_root.left_), self.tree_depth(tree_root.right_)
        if self.is_balance(tree_root.left_) and \
            self.is_balance(tree_root.right_):
            diff = left - right

            if diff <= 1 and diff >= -1:
                # self.depth = 1 + (left if left > right else right)
                return True
        return False

    def tree_depth(self, tree_root):
        if not tree_root:
            return 0

        left = self.tree_depth(tree_root.left_)
        right = self.tree_depth(tree_root.right_)

        return (left + 1) if left > right else (right + 1)

    def is_balance_method_1(self, tree_root):
        self.depth = 0
        return self.is_balance(tree_root)
    # ********************* method 1 **************************

    # ********************* method 2 **************************
    def is_balance_method_2(self, tree_root):
        bool_flag, depth = self.is_balanced(tree_root)
        return bool_flag

    def is_balanced(self, tree_root):
        if not tree_root:
            return True, 0
        bool_left, left_depth = self.is_balanced(tree_root.left_)
        bool_right, right_depth = self.is_balanced(tree_root.right_)

        if bool_left and bool_right:
            diff = left_depth - right_depth
            if -1 <= diff <= 1:
                depth = left_depth
                if diff < 0:
                    depth = right_depth
                return True, depth + 1

        return False, 0
    # **********************************************************


from generate_tree import Generate_tree

def main():
    tree = Generate_tree()
    tree_root = tree.create_tree()
    tree.print_structure()

    # result = Solution_55b().is_balance_method_1(tree_root)
    result = Solution_55b().is_balance_method_2(tree_root)
    if result:
        print('The tree is a balance tree.')
    else:
        print('The tree is not a balance tree.')

if __name__ == '__main__':
    main()

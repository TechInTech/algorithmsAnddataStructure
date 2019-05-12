# -*- coding:utf-8 -*-

"""二叉搜索树的后序遍历序列
"""

class Solution_33(object):

    def verify_squence_of_bst(self, sequence):
        length = len(sequence)
        if length <= 0:
            return False

        split = length-1
        # 在二叉搜索树中左子树节点的值小于根节点的值
        root = sequence[-1]
        for i in range(length-1):
            if sequence[i] > root:
                split = i
                break

        # 在二叉搜索树中右子树节点的值大于根节点的值
        for j in range(split, length-1):
            if sequence[j] < root:
                return False

        # 判断左子树是不是二叉搜索树
        left = True
        if split > 0:
            left = self.verify_squence_of_bst(sequence[0:split])

        # 判断右子树是不是二叉搜索树
        right = True
        if split < length - 1:
            right = self.verify_squence_of_bst(sequence[split:length-1])
            
        return left and right


def main():
    ls = [5, 7, 6, 9, 11, 10, 8]
    length = len(ls)

    s33 = Solution_33()
    result = s33.verify_squence_of_bst(ls)
    if result:
        print('This sequence is a postorder travel sequence.')
    else:
        print('This sequence is not a postorder travel sequence.')


if __name__ == '__main__':
    main()

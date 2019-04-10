# -*- coding:utf-8 -*-

import random
from doubletree import Tree

def get_next_node(p_node):
    if p_node is None:
        warningstr = 'The node is empty.'
        return warningstr

    p_next = None
    if p_node.right_ is not None:
        p_right = p_node.right_
        while p_right.left_ is not None:
            p_right = p_right.left_
        p_next = p_right
    elif p_node.parent_ is not None:
        p_current = p_node
        p_parent = p_node.parent_
        while (p_parent is not None and p_current == p_parent.right_):
            p_current = p_parent
            p_parent = p_parent.parent_
        p_next = p_parent

    return p_next


def get_node_list(tree, L1):
    """Get the list of node by traversing the tree.
    """
    if tree.left_ is not None:
        _ = get_node_list(tree.left_, L1)
    L1.append(tree)    # inorder travel
    if tree.right_ is not None:
        _ = get_node_list(tree.right_, L1)
    return L1


def get_sequence(order):
    while True:
        L1 = input('Input the ' + order +
                   ' sequence (number splitted with \',\' as: 1,2,3,4):')
        if L1 == '':
            print('The sequence is empty, please input again!')
        else:
            sequence = [int(i) for i in L1.split(',')]
            print('The ' + order + ' sequence is:', sequence)
            break
    return sequence


def default_sequence():
    preo = [1, 2, 4, 7, 3, 5, 6, 8]
    ino = [4, 7, 2, 1, 5, 3, 8, 6]
    print('The preorder sequence is:', preo)
    print('The inorder sequence is:', ino)
    return preo, ino


def main():

    choice = input(
        'Enter the y/Y to define two new order sequence, or select the default two order sequence by entering n/N:')
    if choice == 'y' or choice == 'Y':
        sq1 = get_sequence('preorder')
        sq2 = get_sequence('inorder')
    elif choice == 'n' or choice == 'N':
        sq1, sq2 = default_sequence()

    length = len(sq1)

    cls_Tree = Tree()
    Rtree = cls_Tree.gene_tree(sq1, sq2, length)

    L1 = list()
    node_list = get_node_list(Rtree, L1)

    node = node_list[random.randint(0, length - 1)]
    print('The given node is:' + str(node.data_))

    node_next = get_next_node(node)
    print('The value of the next node is: ' + str(node_next.data_))



if __name__ == '__main__':
    main()

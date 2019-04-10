# -*- coding:utf-8 -*-

from tree import Tree


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

    cls_Tree.travel_tree(Rtree)


if __name__ == '__main__':
    main()

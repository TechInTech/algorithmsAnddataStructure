
from generate_tree import Generate_tree

class Solution_36b(object):

    def __init__(self):
        self.plast = None

    def convert(self, tree_root):
        self.convert_node(tree_root)

        phead = self.plast
        while phead and phead.left_:
            phead = phead.left_

        return phead, self.plast

    def convert_node(self, pnode):

        if pnode is None:
            return

        pcurrent = pnode

        if pcurrent.left_:
            self.convert_node(pcurrent.left_)

        pcurrent.left_ = self.plast
        if self.plast:
            self.plast.right_ = pcurrent

        self.plast = pcurrent

        if pcurrent.right_:
            self.convert_node(pcurrent.right_)

def main():
    g_tree = Generate_tree()

    tree_root = g_tree.create_tree()

    g_tree.print_structure()

    doublelink, inv_doublelink = Solution_36b().convert(tree_root)

    print('双向链表升序遍历:')
    while doublelink:
        print(doublelink.data_, end=', ')
        doublelink = doublelink.right_

    print('\n双向链表降序遍历:')
    while inv_doublelink:
        print(inv_doublelink.data_, end=', ')
        inv_doublelink = inv_doublelink.left_

if __name__ == '__main__':
    main()

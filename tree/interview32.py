"""从上到下打印二叉树
"""
from linkedqueue import LinkedQueue
from generate_tree import Generate_tree

class Solution_32(object):

    def __init__(self):
        self.queue = LinkedQueue()

    def printfromtoptobottom(self, treeroot):
        if treeroot is None:
            return None

        self.queue.add(treeroot)
        ret = []
        while not self.queue.isEmpty():
            node = self.queue.pop()
            ret.append(node.data_)
            if node.left_:
                self.queue.add(node.left_)
            if node.right_:
                self.queue.add(node.right_)
        return ret


def main():
    tree = Generate_tree()
    tree_root = tree.create_tree()

    tree.print_structure()

    s32 = Solution_32()
    val_ls = s32.printfromtoptobottom(tree_root)
    print('从上到下打印二叉树:', val_ls)


if __name__ == '__main__':
    main()

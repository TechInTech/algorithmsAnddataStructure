import numpy as np
from linkednode import LinkedNode, Node


def delete_duplication(linkedtable):
    if linkedtable.head is None:
        return

    prenode = None
    pnode = linkedtable.head
    while pnode is not None:
        pnext = pnode.next
        needdelete = False
        if pnext is not None and pnext.data == pnode.data:
            needdelete = True

        if not needdelete:
            prenode = pnode
            pnode = pnode.next
        else:
            value = pnode.data
            ptobedel = pnode
            while ptobedel is not None and ptobedel.data == value:
                pnext = ptobedel.next
                ptobedel = pnext

            if prenode is None:
                linkedtable.head = pnext
            else:
                prenode.next = pnext
            pnode = pnext
    print(linkedtable.__str__())


def main():
    linkedtable = LinkedNode()
    for i in np.random.randint(2, 15, 10).tolist():
        node = Node(i)
        linkedtable.add(node)

    print('The linked node before modified is: ' + linkedtable.__str__())

    delete_duplication(linkedtable)

    print('The linked node after modified is: ' + linkedtable.__str__())


if __name__ == '__main__':
    main()


import numpy as np
from linkednode import LinkedNode, Node


def deletenode(linkedtable, tobedeletednode):
    if linkedtable.head is None or tobedeletednode is None:
        return
    if tobedeletednode.next is not None:
        pnext = tobedeletednode.next
        tobedeletednode.data = pnext.data
        tobedeletednode.next = pnext.next
        pnext = None
    elif linkedtable.head == tobedeletednode:
        tobedeletednode = None
        linkedtable.head = None
    else:
        pnode = linkedtable.head
        while pnode.next is not tobedeletednode:
            pnode = pnode.next
        pnode.next = None
        tobedeletednode = None


def main():
    linkedtable = LinkedNode()
    for i in np.random.randint(2, 15, 10).tolist():
        node = Node(i)
        linkedtable.add(node)

    print('The linked node before modified is: ' + linkedtable.__str__())

    listofnode = linkedtable.listofnode()
    print('The list of node is: ', listofnode)

    tobedeletednode = listofnode[9]

    deletenode(linkedtable, tobedeletednode)

    # print('The value of node to be deleted is %d, and the value of the next closing node is %s' % (tobedeletednode.data, tobedeletednode.next.data))
    print('The linked node after modified is: ' + linkedtable.__str__())


if __name__ == '__main__':
    main()

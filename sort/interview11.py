# -*- coding:utf-8 -*-

def turn_min_1(lst):
    n = len(lst)
    min_val = lst[0]
    i = 1
    while i < n:
        if lst[i] < min_val:
            min_val = lst[i]
        i += 1
    return min_val

def turn_min_2(lst):
    length = len(lst)
    if length <= 0:
        raise KeyError('The list is empty!')
    index1, index2 = 0, length - 1
    dist = index2 - index1
    while dist > 1:
        middle = (index1 + index2) // 2
        if lst[middle] >= lst[index1]:
            index1 = middle
        else:
            index2 = middle
        dist = index2 - index1
    return min(lst[index1], lst[index2])

def turn_min_3(lst):
    if len(lst) <= 0:
        raise KeyError('The list is empty!')
    index1 = 0
    index2 = len(lst) - 1
    indexMid = index1
    while lst[index1] >= lst[index2]:
        if (index2 - index1 == 1):
            indexMid = index2
            break
        indexMid = (index1 + index2) // 2
        if lst[indexMid] >= lst[index1]:
            index1 = indexMid
        else:
            index2 = indexMid
    return lst[indexMid]

def turn_min_4(lst):
    if len(lst) <= 0:
        raise KeyError('The list is empty!')
    index1 = 0
    index2 = len(lst) - 1
    indexMid = index1
    while lst[index1] >= lst[index2]:
        if (index2 - index1 == 1):
            indexMid = index2
            break
        indexMid = (index1 + index2) // 2

        # If the millde number is equal to the first number and second number
        if lst[index1] == lst[index2] and lst[indexMid] == lst[index1]:
            return min_in_order(lst, index1, index2)

        if lst[indexMid] >= lst[index1]:
            index1 = indexMid
        else:
            index2 = indexMid
    return lst[indexMid]

def min_in_order(lst, index1, index2):
    min_val = lst[index1]
    for i in range(index1 + 1, index2 + 1):
        if lst[i] < min_val:
            min_val = lst[i]
    return min_val


def main():
    lst = [3,4,5,1,2]
    lst = [5,6,7,8,9,10,0,1,2,3,4]
    lst = [15,16,17,18,18,20,0,1,2,3,4,5,5,5,5,9,10,11,12,13,14]
    # lst = [1,1,1,0,1]
    # lst = [1,0,1,1,1]

    # min_val = turn_min_1(lst)
    # print('The min value is:', min_val)

    # min_val = turn_min_2(lst)
    # print('The min value is:', min_val)

    # min_val = turn_min_3(lst)
    # print('The min value is:', min_val)

    min_val = turn_min_4(lst)
    print('The min value is:', min_val)

if __name__ == '__main__':
    main()

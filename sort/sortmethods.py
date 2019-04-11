# -*- coding:utf-8 -*-

import random


def sort_insert(lst):
    # for i in range(1, len(lst)):
    #     x = lst[i]
    #     j = i - 1
    #     while j >= 0:
    #         if x >= lst[j]:
    #             break
    #         else:
    #             lst[j + 1] = lst[j]
    #             j -= 1
    #     lst[j + 1] = x
    #     i += 1
    n = len(lst)
    if n == 0:
        raise KeyError('The list is empty.')
    elif n == 1:
        return lst
    else:
        i = 1
        while i < n:
            x = lst[i]
            j = i - 1
            while j >= 0 and x < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = x
            i += 1
    return lst

def swap(lst, i, j):
    temp = lst[j]
    lst[j] = lst[i]
    lst[i] = temp

def sort_select(lst):
    n = len(lst)
    if n == 0:
        raise KeyError('The list is empty.')
    elif n == 1:
        return lst
    else:
        i = 0
        while i < n - 1:
            min_index = i
            j = i + 1
            while j < n:
                if lst[j] < lst[min_index]:
                    min_index = j
                j += 1
            if min_index != i:
                swap(lst, i, min_index)
            i += 1
        return lst


def sort_bubble(lst):
    n = len(lst)
    if n == 0:
        raise KeyError('The list is empty.')
    elif n == 1:
        return lst
    else:
        while n > 1:
            i = 1
            swapped = False
            while i < n:
                if lst[i] < lst[i - 1]:
                    swap(lst, i-1, i)
                    swapped = True
                i += 1
            if not swapped: return lst
            n -= 1
        return lst

def sort_quick(lst):
    quicksort_helper(lst, 0, len(lst) - 1)

def quicksort_helper(lst, left, right):
    if left < right:
        pivotlocation = partition(lst, left, right)
        quicksort_helper(lst, left, pivotlocation - 1)
        quicksort_helper(lst, pivotlocation + 1, right)

def partition(lst, left, right):
    middle = (left + right) // 2
    pivot = lst[middle]
    lst[middle] = lst[right]
    lst[right] = pivot
    boundary = left
    for index in range(left, right):
        if lst[index] < pivot:
            swap(lst, index, boundary)
            boundary += 1
    swap(lst, right, boundary)
    return boundary

def sort_merge(lst):
    copybuffer = [None] * len(lst)
    mergesorthelper(lst, copybuffer, 0, len(lst) - 1)

def mergesorthelper(lst, copybuffer, low, high):
    if low < high:
        middle = (low + high) // 2
        mergesorthelper(lst, copybuffer, low, middle)
        mergesorthelper(lst, copybuffer, middle + 1, high)
        merge(lst, copybuffer, low, middle, high)

def merge(lst, copybuffer, low, middle, high):
    i1, i2 = low, middle + 1
    for i in range(low, high + 1):
        if i1 > middle:
            copybuffer[i] = lst[i2]
            i2 += 1
        elif i2 > high:
            copybuffer[i] = lst[i1]
            i1 += 1
        elif lst[i1] < lst[i2]:
            copybuffer[i] = lst[i1]
            i1 += 1
        else:
            copybuffer[i] = lst[i2]
            i2 += 1

    for i in range(low, high + 1):
        lst[i] = copybuffer[i]


def sort_distr(lst):
    pass

def sort_external(lst):
    pass

def main():

    # lst = [2, 5, 1, 4, 3]
    # print('Before sort:', lst)

    # method 1
    # size = 10000
    # lst = [random.randint(1, size) for i in range(size)]
    # print('Before sort:', lst)
    #
    # lst = sort_insert(lst)
    # print('After sort:', lst)

    # # method 2
    # size = 10000
    # lst = [random.randint(1, size) for i in range(size)]
    # print('Before sort:', lst)
    #
    # lst = sort_select(lst)
    # print('After sort:', lst)

    # # method 3
    # size = 10000
    # lst = [random.randint(1, size) for i in range(size)]
    # print('Before sort:', lst)
    #
    # lst = sort_bubble(lst)
    # print('After sort:', lst)

    # # method 4
    # size = 100000
    # lst = [random.randint(1, size) for i in range(size)]
    # print('Before sort:', lst)
    #
    # sort_quick(lst)
    # print('After sort:', lst)

    # method 5
    size = 100000
    lst = [random.randint(1, size) for i in range(size)]
    print('Before sort:', lst)

    sort_merge(lst)
    print('After sort:', lst)


if __name__ == '__main__':
    main()

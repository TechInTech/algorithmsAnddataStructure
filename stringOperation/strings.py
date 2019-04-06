# -*- coding:utf-8 -*-
import copy

# the general algorithm of string matching


def string_matching(tar_str, pat_str, pos):
    i = pos
    j = 0
    while i < (len(tar_str) - 1):
        k = copy.copy(i)
        while tar_str[k] == pat_str[j]:
            k += 1
            j += 1
            if j == len(pat_str):
                return True, i
            if (len(pat_str) - j) > (len(tar_str) - k):
                return False, None
        i += 1
        j = 0
    return False, None

# data structure and algorithm
# -> native match string


def native_match(t, p):
    m, n = len(t), len(p)
    i, j = 0, 0
    while i < m and j < n:
        if t[i] == p[j]:
            i, j = i + 1, j + 1
        else:
            i, j = i - j + 1, 0
    if j == n:
        return i - j
    return -1

# KMP (string matching Algorithm)


def kmp_matching(t, p):
    m, n = len(t), len(p)
    i, j = 0, 0
    while i < m and j < n:
        if j == -1 or t[i] == p[j]:
            i, j = i + 1, j + 1
        else:
            j = pnext[j]
    if j == n:
        return i - j
    return -1


def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            k, i = k + 1, i + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext


def gen_pnext_pro(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            k, i = k + 1, i + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext

# To judge whether the input is empty


def condition(str_):
    if str_ == '':
        print('The string can\'t empty!\n')
        return True
    return False

# input the string


def input_string(action):
    while True:
        input_str = input('Please input the ' + action + ' string:\n' + '-->')
        if not condition(input_str):
            return input_str

# input the string and the start posit, and considering possible unexceptive input


def recieve_string():

    print('***** Please follow the steps to input the strings and position. *****\n')

    action1 = 'target'
    str1 = input_string(action1)    # target strings

    action2 = 'pattern'
    str2 = input_string(action2)    # pattern strings

    while len(str1) < len(str2):    # the length of target strings should longer than the pattern's
        print('The target string\'s length is shorter than the pattern string\'s, please input again!\n')
        str2 = input_string(action2)

    while True:
        try:
            # when the input isn't a number, tell the user to enter a nuber.
            pos = int(input('Please input the statr position to search'
                            + '(0 <= pos <=' + str(len(str1) - 1) + '):\n' + '-->'))
            if pos > len(str1) - 1:
                print('The position is larger than ' +
                      str(len(str1) - 1) + '!\n')
                continue
            break
        except ValueError:
            print('Please confirm what input is a number!')
            continue

    return str1, str2, pos


def main():
    str1, str2, pos = recieve_string()
    print(' The target string: %s' % str1, '\n', 'The pattern string: %s' %
          str2, '\n', 'The start position: %d' % pos)
    # if str2 is matching to str1, return True and the index.
    label, local_index = string_matching(str1, str2, pos)
    if label:
        print('The pattern string can match the target string, and the start index is '
              + str(local_index) + ' !')
    else:
        print('Sorry，the pattern string can\'t match the target string!')


if __name__ == '__main__':
    main()

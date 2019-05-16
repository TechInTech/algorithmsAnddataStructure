# -*- coding:utf-8 -*-
"""左旋转字符串
"""

class Solution_58b(object):
    def left_rotate_str(self, s, n):
        if not s or len(s) <= 0 or n < 0:
            return None

        length = len(s)
        str_ls = list(s)

        if length > 0 and n < length and n > 0:
            firststart, firstend = 0, n - 1
            secondstart, secondend = n, length - 1

            str_ls = self.reverse(str_ls, firststart, firstend)
            str_ls = self.reverse(str_ls, secondstart, secondend)
            str_ls = self.reverse(str_ls, firststart, secondend)
        result = ''.join(str_ls)
        return result

    def reverse(self, str_ls, begin, end):
        if not str_ls or len(str_ls) <= 0:
            return ''

        while begin < end:
            str_ls[begin], str_ls[end] = str_ls[end], str_ls[begin]
            begin += 1
            end -= 1
        return str_ls


def main():

    string = 'abcdefg'
    n = 2

    result = Solution_58b().left_rotate_str(string, n)

    if result:
        print('The reverse string is: ', result)
    else:
        print('The string is invalid.')


if __name__ == '__main__':
    main()

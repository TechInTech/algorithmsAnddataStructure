# -*- coding:utf-8 -*-
"""翻转字符串
"""

class Solution_58(object):
    def __init__(self, s=None):
        self.str = s

    def reverse(self, str_ls):
        if not str_ls or len(str_ls) <= 0:
            return ''

        begin, end = 0, len(str_ls) - 1
        while begin < end:
            str_ls[begin], str_ls[end] = str_ls[end], str_ls[begin]
            begin += 1
            end -= 1
        return str_ls

    def reverse_sentence(self):
        if not self.str or len(self.str) <= 0:
            return ''

        begin, end = 0, len(self.str) - 1

        str_ls = list(self.str)
        str_ls = self.reverse(str_ls)

        begin = end = 0

        result_str = ''
        list_tem = []

        while end < len(str_ls):
            if end == len(str_ls) - 1:
                list_tem.extend(self.reverse(str_ls[begin:]))
                break
            if str_ls[begin] == " ":
                begin += 1
                end += 1
                list_tem.extend(' ')
            elif str_ls[end] == ' ':
                list_tem.extend(self.reverse(str_ls[begin:end]))
                begin = end
            else:
                end += 1

        result_str += "".join(list_tem)
        return result_str

    # method 2
    def reverse2(self, s):
        """利用python的切分语句实现
        """
        ls = s.split(' ')
        return ' '.join(ls[::-1])

def main():

    string = 'I am a student.'

    result = Solution_58(string).reverse_sentence()
    # result = Solution_58().reverse2(string)
    if result:
        print('The reverse string is: ', result)
    else:
        print('The string is invalid.')


if __name__ == '__main__':
    main()

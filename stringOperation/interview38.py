# -*- coding: utf-8 -*-

"""字符串排序
"""

class Solution_38(object):
    def __init__(self):
        self.result = []

    def permutation(self, strings):
        if not strings:
            return []
        str_ls = list(strings)

        self.permute(str_ls, 0)

        # 由于输入字符中可能存在重复的字符，所以最终排序中有重复的序列，故最终结果应该去重、排序
        res = list(set(self.result))
        res.sort()
        return res

    def permute(self, string, begin):
        # 最后一个字符
        if begin == len(string):
            self.result.append(''.join(string))
        else:
            for i in range(begin, len(string)):
                # 将首字符与余下字符进行交换
                string[i], string[begin] = string[begin], string[i]
                # 固定首位，递归余下部分
                self.permute(string, begin+1)
                # 将交换的字符换回来
                string[begin], string[i] = string[i], string[begin]

def main():
    in_str = 'abcad'

    s38 = Solution_38().permutation(in_str)
    print('For string \'' + in_str +'\', the possible sort are following:')
    print(s38)


if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-
"""第一个只出现一次的字符
"""
import time

class Solution_50(object):
    def first_not_repeating_char(self, s):

        if s is None or s == '':
            return None

        char_dict = {}
        for i in s:
            if i in char_dict.keys():
                char_dict[i] += 1
            else:
                char_dict[i] = 1

        for i in char_dict.keys():
            if char_dict[i] == 1:
                return i
        return None

    def first_not_repeating_char_2(self, s):

        if s is None or s == '':
            return None

        char_ls = []
        for i in s:
            if i in char_ls:
                continue
            num = s.count(i)
            if num == 1:
                return i
            else:
                char_ls.append(i)
        return None


def main():
    s = 'abaccdeffdirpposjdklmnhhxixaccdeffdirpposjdklmnhhxixaccdeffdirpposjdklmnhhxixaccdeffdirpposjdklmnhhxixaccdeffdirpposjdklmnhhxixaccdeffdirpposjdklmnhhxixaccdeffdirpposjdklmnhhxixaccdeffdirpposjdklmnhhxix'

    t1 = time.time()
    result = Solution_50().first_not_repeating_char_2(s)

    print('Consumed time: %f'%(time.time()-t1))
    print(result)

if __name__ == '__main__':
    main()

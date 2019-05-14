# -*- coding:utf-8 -*-
"""最长不含重复字符的子字符串
"""

class Solution_48(object):
    def longest_substring_without_duplication(self, string):
        curr_length = 0
        max_length = 0

        position = [-1] * 26

        for i in range(len(string)):
            pre_index = position[ord(string[i]) - ord('a')]
            if pre_index < 0 or (i - pre_index > curr_length):
                curr_length += 1
            else:
                if curr_length > max_length:
                    max_length = curr_length

                curr_length = i - pre_index
            position[ord(string[i]) - ord('a')] = i

        if curr_length > max_length:
            max_length = curr_length

        del position
        return max_length


def main():
    s = 'arabcacfr'

    max_length = Solution_48().longest_substring_without_duplication(s)

    print('The maximum length is %d.'%max_length)


if __name__ == '__main__':
    main()

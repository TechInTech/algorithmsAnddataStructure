# -*- coding:utf-8 -*-
"""字符流中第一个只出现一次的字符
"""

class Solution_50b(object):
    def __init__(self):
        self.stream = []
        self.counter = {}

    def first_appearing_once(self):
        if len(self.stream) <= 0:
            return None
        for s in self.stream:
            if self.counter[s] == 1:
                return s
        return None

    def insert_str(self, s):
        if s in self.stream:
            self.counter[s] += 1
        else:
            self.counter[s] = 1
        self.stream.append(s)


def main():
    s = 'google'

    s50b = Solution_50b()

    for i in s:
        s50b.insert_str(i)

    result = s50b.first_appearing_once()
    print('The fisrt appearing once string is:', result)


if __name__ == '__main__':
    main()

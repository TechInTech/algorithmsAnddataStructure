# -*- coding:utf-8 -*-
"""圆圈中最后剩下的数字
"""

class Solution_62(object):
    def __init__(self):
        self.current = 0
        self.next = 0

    def last_remaining(self, n, m):
        """
        n: 环链表中的元素个数
        m: 删除的第m个元素
        """
        if n < 1 or m < 1:
            # 环元素个数小于1时，输出‘-1’表示异常
            return -1

        numbers = [i for i in range(n)]

        while len(numbers) > 1:
            for i in range(1, m):
                self.current += 1
                if self.current == len(numbers):
                    self.current = 0
            self.next = self.current + 1

            if self.next == len(numbers):
                self.next = 0

            if self.current == len(numbers) - 1:
                # current 在最后一个元素，删除current所在元素后，current为列表首位，
                # next为current下一位
                del numbers[self.current]
                self.current = 0
                self.next = self.current + 1
            elif self.current == len(numbers) - 2:
                # current为列表倒数第二位，删除current后，current为列表最后一位，next为表首
                del numbers[self.current]
                self.next = 0
            else:
                # current在列表中时，删除current后，current所在位置不变，next减1
                del numbers[self.current]
                self.next -= 1

        return numbers[self.current]


def main():
    n, m = 5, 3
    result = Solution_62().last_remaining(n, m)
    print('The last number is %d.'%result)


if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-
"""丑数
   > 定义：把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但7、
   14不是，因为它们包含质因子7。 习惯上我们把1当做是第一个丑数。

   > 判断：首先除2，直到不能整除为止，然后除5到不能整除为止，然后除3直到不能整除为止。
   最终判断剩余的数字是否为1，如果是1则为丑数，否则不是丑数。
"""

class Solution_49(object):
    # method 1
    def get_ugly_number(self, n):
        """
        n: 为给定的索引大小
        """
        if n <= 0:
            return 0

        number = 0
        ugly_found = 0

        while ugly_found < n:
            number += 1
            if self.is_ugly(number):
                ugly_found += 1

        return number

    def is_ugly(self, num):
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        return True if num == 1 else False

    # method 2
    def get_ugly_number_2(self, n):
        if n <= 0:
            return 0

        pugly_ls = [1] # 1为第一个丑数

        next_index = 1

        min2, min3, min5 = 0, 0, 0

        while next_index < n:
            min_num = min(pugly_ls[min2] * 2, pugly_ls[min3] * 3, pugly_ls[min5] * 5)
            pugly_ls.append(min_num)

            # 找到第一个乘以2的结果大于当前最大丑数M的数字，也就是T2
            while pugly_ls[min2] * 2 <= min_num:
                min2 += 1

            # 找到第一个乘以3的结果大于当前最大丑数M的数字，也就是T3
            while pugly_ls[min3] * 3 <= min_num:
                min3 += 1

            # 找到第一个乘以5的结果大于当前最大丑数M的数字，也就是T5
            while pugly_ls[min5] * 5 <= min_num:
                min5 += 1

            next_index += 1

        return pugly_ls[-1]


def main():
    n = 1000

    result = Solution_49().get_ugly_number_2(n)

    print('第%d个丑数为%d'%(n, result))



if __name__ == '__main__':
    main()

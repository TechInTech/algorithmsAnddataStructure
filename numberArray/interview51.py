# -*- coding:utf-8 -*-
"""数组中的逆序对
"""
import copy

class Solution_51(object):
    def inverse_pairs(self, data):
        length = len(data)
        if length <= 0 or data is None:
            return 0

        data_2 = copy.deepcopy(data)

        count = self.inverse_pairs_core(data, data_2, 0, length -1)
        del data_2

        return count

    def inverse_pairs_core(self, data, data_2, start, end):
        if start == end:
            data_2[start] = data[start]
            return 0

        length = (end - start) // 2

        left = self.inverse_pairs_core(data_2, data, start, start + length)
        right = self.inverse_pairs_core(data_2, data, start + length + 1, end)

        i = start + length
        j = end

        index_copy = end
        count = 0

        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                data_2[index_copy] = data[i]
                index_copy -= 1
                i -= 1
                count += j - start -length
            else:
                data_2[index_copy] = data[j]
                index_copy -= 1
                j -= 1

        while i >= start:
            data_2[index_copy] = data[i]
            index_copy -= 1
            i -= 1
        while j >= start + length + 1:
            data_2[index_copy] = data[j]
            index_copy -= 1
            j -= 1

        return left + right + count


def main():

    array = [7, 5, 6, 4]

    result = Solution_51().inverse_pairs(array)
    print('The count are %d'%result)


if __name__ == '__main__':
    main()

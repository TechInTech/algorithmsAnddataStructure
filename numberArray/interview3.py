# -*- coding:utf-8 -*-

import time

# Finding the repeated number in array.

def count_range(array, length, start, end):
    count = 0
    for i in range(length):
        if array[i] >= start and array[i] <= end:
            count += 1
    return count

def search_method4(array):
    """Don\'t modify the array, finding the repeated number.
    """
    m = len(array)
    start = 1
    end = m - 1
    while start <= end:
        mid = (end - start) // 2 + start
        count = count_range(array, m, start, mid)
        if start == end:
            if count > 1:
                return start
            else:
                break
        if count > (mid - start + 1):
            end = mid
        else:
            start = mid + 1
    return -1

def search_method3(array):
    m = len(array)
    rep_number = []
    for i in range(m):
        if array[i] in rep_number:
            continue
        else:
            for j in range(i + 1, m):
                if array[i] == array[j]:
                    if array[i] not in rep_number:
                        rep_number.append(array[i])
    if len(rep_number) == 0:
        warningstr = 'The array is not repeated'
        return False, warningstr
    else:
        return True, rep_number

def search_method1(array):
    m = len(array)
    rep_number = {}
    for i in range(m):
        if array[i] is None:
            continue
        else:
            for j in range(i + 1, m):
                if array[i] == array[j]:
                    if array[i] in rep_number.keys():
                        rep_number[array[i]] += 1
                    else:
                        rep_number[array[i]] = 0
                    array[j] = None
    if rep_number == {}:
        warningstr = 'The array is not repeated'
        return False, warningstr
    else:
        rep_number = [int(key) for key in rep_number.keys()]
        return True, rep_number

def search_method2(array):
    rep_number = []
    m = len(array)
    for i in range(len(array)):
        while True:
            if array[i] == i:
                break
            elif array[i] < m:
                if array[array[i]] == array[i]:
                    if array[i] not in rep_number:
                        rep_number.append(array[i])
                    break
                else:
                    temp = array[i]
                    array[i] = array[temp]
                    array[temp] = temp
            else:
                warningstr = 'There are number beyond the range from 0 to ' + str(m -1) + ', please input again!'
                return False, warningstr
    if len(rep_number) == 0:
        warningstr = 'The array is not repeated'
        return False, warningstr
    else:
        return True, rep_number

def judge_fun(array):
    array.sort()
    m = len(array)
    warningstr = None
    if array[-1] >= m:
        warningstr = 'There are number beyond the range from 0 to ' + str(m -1) + ', please input again!'
        return True, warningstr
    else:
        return False, warningstr

def main():
    while True:
        L1 = input('Input the testing array(number splitted with \',\' as: 1,2,3,4):')
        if L1 == '':
            print('The array is empty, please input again!')
        else:
            dataarray = [int(i) for i in L1.split(',')]
            print('The input array is:', dataarray)

            """ Combine with method 1 to judge whether the input beyond
            the range 0 ~ len(dataarray) - 1
                ******************************************
            """
            # resu_label, resu_str = judge_fun(dataarray)
            # if resu_label:
            #     print(resu_str)
            #     continue
            # else:
            """ ****************************************** """
            break
    t1 = time.time()

    # ret, number = search_method1(dataarray) # method 1

    # ret, number = search_method2(dataarray) # method 2

    # ret, number = search_method3(dataarray) # method 3

    # if ret:
    #     print('There are %d repeated numbers.' % len(number))
    #     print('The number is:', number)
    # else:
    #     print(number)
    # t2 = time.time()
    # print('consume time: %f' % (t2 - t1))


    # method 4
    ret = search_method4(dataarray) # method 4
    if ret == -1:
        print('There exist not repeated number in array!')
    else:
        print('The repeated number is %d' % ret)

if __name__ == '__main__':
    main()

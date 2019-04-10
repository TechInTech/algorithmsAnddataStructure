# -*- coding:utf-8 -*-


def sort_array(array1, array2):
    array1.sort()
    array2.sort()
    m1 = len(array1)
    m2 = len(array2)
    j = m1 - 1
    i = m2 - 1
    while i >= 0:
        if array2[i] >= array1[j]:
            array1.insert(j + 1, array2[i])
            i -= 1
        else:
            if j == 0:
                array1.insert(j, array2[i])
                i -= 1
            else:
                j -= 1
    return array1


def get_array(num):
    while True:
        L1 = input('Input the array ' + num +
                   '(number splitted with \',\' as: 1,2,3,4):')
        if L1 == '':
            print('The input is empty, please input again!')
        else:
            array = [int(i) for i in L1.split(',')]
            print('The array ' + num + ' is:', array)
            break
    return array


def main():
    a1 = get_array('A1')
    a2 = get_array('A2')

    ret = sort_array(a1, a2)
    print('After the array a2 insert a1, the entire array is:', ret)


if __name__ == '__main__':
    main()

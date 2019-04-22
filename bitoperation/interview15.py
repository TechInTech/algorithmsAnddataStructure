import copy

def inttobin(integer):
    binarylist = list()
    if integer == 0 :
        return 0, str(0)
    while integer >= 1:
        integer, y = divmod(integer, 2)
        binarylist.insert(0, y)

    countnum = binarylist.count(1)
    length = len(binarylist)
    binary = ''
    for i in range(length):
        binary += str(binarylist[i])
    return countnum, binary


def numberof1(n):
    count = 0
    while n:
        count += 1
        n = (n - 1) & n
    return count


def numberof2(m, n):
    count = 0
    mn = m ^ n
    while mn:
        count += 1
        mn = (mn - 1) & mn
    return count


def main():
    # integer = int(input('Input the integer:'))

    # countnum, binary = inttobin(integer)
    # print('The binary of input integer is ' + binary + ', and the number of \'1\' in binary is %s' % countnum)

    # num = numberof1(integer)
    # print('The number is %d' % num)
    #
    # if num != 1:
    #     print('The input integer is not the integer power of 2!')
    # else:
    #     print('The input integer is the integer power of 2!')

    m, n = 10, 13
    num = numberof2(m, n)
    print('The times needed to change is %d' % num)


if __name__ == '__main__':
    main()

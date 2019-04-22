
def print_1_to_max_of_n_digits(n):
    if n <= 0:
        return
    number = [0] * n

    while not increment(number):
        printnumber(number)


def increment(number):
    isoverflow = False
    ntakeover = 0
    nlength = len(number)

    for i in range(nlength - 1, -1, -1):
        nsum = number[i] + ntakeover
        # print(nsum)
        if i == (nlength - 1):
            nsum += 1
        if nsum >= 10:
            if i == 0:
                isoverflow = True
            else:
                nsum -= 10
                ntakeover = 1
                number[i] = nsum
        else:
            number[i] = nsum
            break
    return isoverflow


def printnumber(number):
    isbeginning0 = True
    nlength = len(number)

    if nlength == 1:
        print('%d' % number[0])
    else:
        for i in range(nlength):
            if isbeginning0 and (i != nlength - 1):
                isbeginning0 = False

            if not isbeginning0:
                # pass
                print('%d' % number[i])
    print('\t')


def print_1_to_max_of_n_digits2(n):
    if n <= 0:
        return
    number = [0] * n

    for i in range(10):
        number[0] = i
        print_1_to_max_of_n_digits_recursively(number, n, 0)


def print_1_to_max_of_n_digits_recursively(number, length, index):
    if index == length - 1:
        printnumber(number)
        return

    for i in range(10):
        number[index + 1] = i
        print_1_to_max_of_n_digits_recursively(number, length, index + 1)


def main():

    n = int(input("please input the integer:"))

    print_1_to_max_of_n_digits(n)

    # print_1_to_max_of_n_digits2(n)


if __name__ == '__main__':
    main()

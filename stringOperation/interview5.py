# -*- coding:utf-8 -*-

def replace_fun(string, str1):
    if string == '':
        warningstr = 'The string is empty.'
        return False, warningstr
    m = len(string)
    p = (m - 1)
    label = True
    while p >= 0:
        if string[p] == ' ':
            if p == 0:
                string = str1 + string[1:]
            elif p == m -1:
                string = string[0:p] + str1
            else:
                string = string[0:p] + str1 + string[p + 1:]
            label = False
        p -= 1
    if label:
        warningstr = 'There is not a space in the string.'
        return False, warningstr
    else:
        return True, string

def main():
    tar_str = input('Please input the target strings(with space):')

    print('*************** Before modify ******************')
    print('The input string is: ' + tar_str)
    print('The length of input string is: ' + str(len(tar_str)))

    rpl_str = '%20'
    ret, modified_str = replace_fun(tar_str, rpl_str)

    print('***************  After modify ******************')
    if ret:
        print('The string after replacing is: ' + modified_str)
        print('The length of modified string is: ' + str(len(modified_str)))
    else:
        print(modified_str)

if __name__ == '__main__':
    main()


# import copy
class Solution(object):
    def __init__(self):
        self.cursor = 0

    def isnumeric(self, string):
        if not string:
            return False

        numeric = self.scaninteger(string)

        if self.cursor < len(string) and string[self.cursor]  == '.':
            self.cursor += 1

            numeric = self.scanunsignedinteger(string) or numeric

        if self.cursor < len(string) and (string[self.cursor] == 'e' or string[self.cursor] == 'E'):
            self.cursor += 1

            numeric = numeric and self.scaninteger(string)

        return numeric and self.cursor == len(string)


    def scanunsignedinteger(self, string):
        before = self.cursor

        while self.cursor < len(string) and string[self.cursor] >= '0' and string[self.cursor] <= '9':
            self.cursor += 1

        return self.cursor > before


    def scaninteger(self, string):
        if string[self.cursor] == '+' or string[self.cursor] == '-':
            self.cursor += 1

        return self.scanunsignedinteger(string)


def main():
    string = input('Input the string:')
    todecide = Solution()
    label = todecide.isnumeric(string)

    if label:
        print('The string represent the numeric!')
    else:
        print('The string do not represent the numeric!')


if __name__ == '__main__':
    main()


def match(string, pattern):
    if string is None or pattern is None:
        return False

    return matchcore(string, pattern)


def matchcore(string, pattern):
    if string == '' and pattern == '':
        return True

    if string != '' and pattern == '':
        return False

    if pattern[1] == '*':
        if pattern[0] == string[0] or (pattern[0] == '.' and len(string) != 0):
            return matchcore(string + 1, pattern + 2) or matchcore(string + 1, pattern) or\
             matchcore(string, pattern + 2)
        else:
            return matchcore(string, pattern + 2)
    if string == pattern or (pattern == '.' and len(string) != 0):
        return matchcore(string + 1, pattern + 1)

    return False


def main():
    string = input('Input the string:')
    pattern = input('Input the pattern string:')

    label = matchcore(string, pattern)
    if label:
        print('The string can match the pattern string!')
    else:
        print('The string can not match the pattern string!')

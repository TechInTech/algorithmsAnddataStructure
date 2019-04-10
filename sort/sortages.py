# -*- coding:utf-8 -*-

def sortages(ageslist):
    length = len(ageslist)

    if length == 0:
        raise KeyError('The list of ages is empty.')

    maxage = 99
    timesofage = [0] * (maxage + 1)

    for i in range(maxage + 1):
        age = ageslist[i]
        if age < 0 or age > maxage:
            raise KeyError('The age is disnormal.')
        timesofage[i] += 1
    index = 0
    for i in range(maxage + 1):
        for j in range(timesofage[i]):
            ageslist[index] = i
            index += 1    

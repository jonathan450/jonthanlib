#
# put here all the definitions for specific fromulas.
#

import math


def fibon_sequence(n):
    x = 1
    y = 1
    cont = 1
    while cont <= n:
        print('A new fibon number is ', x + y)
        temp = x
        x = y
        y = y + temp
        cont = cont + 1


def distance2d(x1, y1, x2, y2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d


def distance3d(x1, y1,z1, x2, y2, z2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2+ (z1-z2)**2)
    return d

def convert_list_to_word(alist):
    new_word = ""

    n = len(alist)
    for I in range(n):
        new_word = new_word + alist[I]
    return new_word


def eliminate_repeats(oldlist):
    new_list = []
    for letter in alist:
        if letter not in new_list:
            new_list.append(letter)

    return new_list


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    magdict = dict()
    notedict = dict()

    for m in magazine:
        if m not in magdict:
            magdict[m] = 1
        else:
            magdict[m] += 1

    for n in note:
        if n not in notedict:
            notedict[n] = 1
        else:
            notedict[n] += 1

    if all(item in magdict.items() for item in notedict.items()):
        print('Yes')
    else:
        print('No')





if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

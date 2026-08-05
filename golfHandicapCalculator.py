'''
Given an array of golf scores and a corresponding array of course par values, return the golfer's handicap index using the following method:

Calculate the differential for each round by subtracting the par from the score, then return the average of all differentials rounded to one decimal place.
'''

import math
def calculate_handicap(scores, pars):

    differential = [score - par for score,par in zip(scores, pars)]
    avg = sum(differential) / len(differential)
    return math.floor(avg * 10 + 0.5) / 10



print(calculate_handicap([72, 72, 72], [72, 72, 72])) # should return 0.
print(calculate_handicap([80, 76, 78, 78], [72, 72, 72, 72])) # should return 6.
print(calculate_handicap([42, 45, 46, 44], [36, 36, 36, 36])) # should return 8.3.
print(calculate_handicap([85, 80, 76, 79, 82], [72, 72, 72, 71, 71])) # should return 8.8.
print(calculate_handicap([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37])) # should return 11.7.
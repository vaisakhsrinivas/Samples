'''
Given an integer, n, return the number of valid combinations of n pairs of parentheses.

A valid combination is a string where every opening parentheses has a corresponding closing parentheses, and no closing parentheses appears before its matching opening parentheses.
For example, given 2, there are 2 valid combinations:
'''

def get_combinations(n):

    count = 0

    def bktrk(op, close):

        nonlocal count
        if op == n and close == n:
            count += 1
            return
        if op < n:
            bktrk(op+1, close)
        if close < op:
            bktrk(op, close+1)
    bktrk(0,0)
    return count



get_combinations(2) # should return 2.
get_combinations(3) # should return 5.
get_combinations(5) # should return 42.
get_combinations(8) # should return 1430.
get_combinations(13) # should return 742900.

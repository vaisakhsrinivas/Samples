'''
Given a number, determine whether it is a pronic number.

A pronic number is the product of two consecutive integers. For example, 6 is pronic because 2 * 3 = 6.
'''


def is_pronic(number):

    i = 0
    while i * (i+1) <= number:
        if i * (i+1) == number:
            return True
        i += 1
    return False



print(is_pronic(6)) #should return True.
print(is_pronic(15)) #should return False.
print(is_pronic(12)) #should return True.
print(is_pronic(132)) #should return True.
print(is_pronic(80)) #should return False.
print(is_pronic(0)) #should return True.
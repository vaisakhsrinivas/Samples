'''
Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many hours of sleep you need tonight to eliminate your sleep debt.

Include tonight's hours in the total time needed to catch up.
If you've slept enough to cover tonight's target or more, return 0.
'''


def sleep_debt(hours_slept, target_hours):

    totaltarget = (len(hours_slept) + 1) * target_hours
    currentslept = sum(hours_slept)
    if currentslept < totaltarget:
        dept = totaltarget - currentslept
        return dept
    return 0

print(sleep_debt([6, 6, 6, 6, 6, 6], 8)) #should return 20.
print(sleep_debt([6, 7, 8, 4, 8, 6], 7))#should return 10.
print(sleep_debt([10, 10, 9, 10, 9, 11], 9)) #should return 4.
print(sleep_debt([8, 7, 6, 7, 6, 8], 6)) #should return 0.
print(sleep_debt([8, 9, 10, 9, 10, 7], 7)) #should return 0.
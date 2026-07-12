'''
Given an array of five dice with values 1-6, return the best possible hand.

Here are the hands ranked lowest to highest:

Hand	Description
"no pair"	No pair or better
"pair"	Two dice with the same value
"two pair"	Two different pairs
"three of a kind"	Three dice with the same value
"small straight"	Four consecutive values
"large straight"	Five consecutive values
"full house"	Three of a kind and a pair
"four of a kind"	Four dice with the same value
"five of a kind"	All five dice with the same value
'''

from Unique import unique
def five_dice(dice):

    dice = sorted(dice)
    counts = []

    for value in set(dice):
        counts.append(dice.count(value))
    counts.sort(reverse=True)

    unique = sorted(set(dice))

    if counts[0] == 5:
        return "five of a kind"
    if counts[0] == 4:
        return "four of a kind"
    if counts[0] == 3 and counts[1] == 2:
        return "full house"
    if len(unique) == 5 and unique[-1] - unique[0] == 4:
        return "large straight"
    if any(unique[i+3] - unique[i] == 3 and unique[i+3] - unique[i+1] == 2 and unique[i+1] - unique[i] == 1 for i in range(len(unique)-3)):
        return "small straight"
    if counts[0] == 3:
        return "three of a kind"
    if counts[0] == 2 and counts[1] == 2:
        return "two pair"
    if counts[0] == 2:
        return "pair"
    return "no pair"


print(five_dice([1, 1, 1, 1, 1])) #should return "five of a kind".
print(five_dice([5, 5, 5, 6, 5])) #should return "four of a kind".
print(five_dice([2, 5, 6, 4, 3])) #should return "large straight".
print(five_dice([4, 3, 3, 3, 1])) #should return "three of a kind".
print(five_dice([4, 6, 2, 6, 5])) #should return "pair".
print(five_dice([1, 4, 5, 6, 2])) #should return "no pair".
print(five_dice([1, 3, 4, 6, 2])) #should return "small straight".
print(five_dice([2, 2, 5, 2, 5])) #should return "full house".
print(five_dice([6, 4, 5, 6, 4])) #should return "two pair".

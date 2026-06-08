def last_load_date(scoops, usage):
    l = len(usage)
    avguse = sum(usage) / l
    remainingdays = int(scoops // avguse)

    return remainingdays

print(last_load_date(10, [2, 2, 2, 2, 2, 2, 2])) # should return 5.
print(last_load_date(16, [2, 3, 0, 3, 4, 2, 1]) ) #should return 7
print(last_load_date(33, [5, 0, 4, 3, 3, 2])) #should return 11.
print(last_load_date(50, [2, 0, 2, 9, 12, 0, 2])) #should return 12.
print(last_load_date(20, [13, 9, 12, 10, 8])) #should return 1.
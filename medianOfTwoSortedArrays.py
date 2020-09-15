def findMedianSortedArrays(nums1, nums2):
    nlist = []
    for item in nums1:
        nlist.append(item)
    for item in nums2:
        nlist.append(item)
    nlist.sort()
    if len(nlist) % 2 != 0:
        return nlist[len(nlist)//2]
    else:
        return (nlist[len(nlist)//2] + nlist[len(nlist)//2 - 1])/2



nums1 = [1,2]
nums2 = [3]

print(findMedianSortedArrays(nums1, nums2))
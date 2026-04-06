def intersection_of_arrays(nums1, nums2):
    count1 ={}
    result = []
    for i in nums1:
        count1[i] = count1.get(i,0)+1

    for j in nums2:
        if j in count1 and count1[j] > 0:
            result.append(j)
            count1[j] -= 1
    return result
            
        

if __name__ == "__main__":
    nums1 = [int(x) for x in input().split()]
    nums2 = [int(x) for x in input().split()]
    res = intersection_of_arrays(nums1, nums2)
    print(" ".join(map(str, res)))

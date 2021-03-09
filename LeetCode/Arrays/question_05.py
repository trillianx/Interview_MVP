def merge(nums1, m, nums2, n):
    result = []
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        elif nums1[i] >= nums2[j]:
            result.append(nums2[j])
            j += 1
    result += nums1[i:m] + nums2[j:n]
    return result

if __name__=='__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    result = merge(nums1, m, nums2, n)
    print(result)

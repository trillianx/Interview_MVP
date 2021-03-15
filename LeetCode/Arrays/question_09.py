def valid_mountain(arr):
    n = len(arr)
    difference = []
    for i in range(1, n):
        difference.append(arr[i-1] - arr[i])
    # Find the pivot
    pivot_index = 0
    for index, i in enumerate(difference):
        if i >= 0:
            pivot_index = index
            break
    if pivot_index == 0:
        return False
    # Start with pivot and see whether
    # at any point we have a negative value
    while pivot_index < n:
        if difference[pivot_index] < 0:
            return False
        pivot_index += 1
    return True
    
if __name__=='__main__':
    arr = [0, 2, 3, 4, 5, 2, 1, 0]
    arr2 = [0, 2, 3, 3, 5, 2, 1, 0]
    result = valid_mountain(arr)
    print(result)
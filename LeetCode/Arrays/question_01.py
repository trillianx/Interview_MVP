def findMaxConsecutiveOnes(arr):
    n = len(arr)
    max_length = 0
    count = 0
    for n in arr:
        if n == 1:
            count += 1
        else:
            max_length = max(max_length, count)
            count = 0
    max_length = max(max_length, count)
    return max_length


if __name__=='__main__':
    arr = [0, 0, 0, 1, 0]
    result = findMaxConsecutiveOnes(arr)
    print(result)

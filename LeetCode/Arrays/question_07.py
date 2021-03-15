def remove_duplicates(arr):
    n = len(arr)
    start = 0
    for end in range(1, n):
        if arr[start] != arr[end]:
            start += 1
            arr[start] = arr[end]
    return arr

if __name__=='__main__':
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = remove_duplicates(arr)
    print(result)
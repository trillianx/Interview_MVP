def remove_element(arr, value):
    n = len(arr)
    start = 0
    while start < n:
        if arr[start] == value:
            arr[start], arr[n-1] = arr[n-1], arr[start]
            n -= 1
        else:
            start += 1
    return n

if __name__=='__main__':
    arr = [3, 2, 2, 3]
    result = remove_element(arr, 2)
    print(result)
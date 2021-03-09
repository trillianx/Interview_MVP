def duplicateZeros(arr):
    insert_list = []
    for index, i in enumerate(arr):
        if i == 0:
            insert_list.append(index)
            arr.pop()
    count = 1
    for i in insert_list:
        insert_val = i + count
        arr.insert(insert_val, 0)
        count += 1
    return arr

if __name__=='__main__':
    arr = [0, 1]
    result = duplicateZeros(arr)
    print(result)
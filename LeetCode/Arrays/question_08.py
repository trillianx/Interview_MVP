def find_double(arr):
    seen = set()
    for val in arr:
        if 2*val in seen or 0.5*val in seen:
            return True
        seen.add(val)
        
    return False

if __name__=='__main__':
    arr = [3,1,7,11]
    arr2 = [-10,12,-20,-8,15]
    result = find_double(arr2)
    print(result)
        
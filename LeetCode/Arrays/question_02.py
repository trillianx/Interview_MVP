def find_numbers(nums):
    n = len(nums)
    count = 0
    for num in nums:
        this_num = str(num)
        length = len(this_num)
        if length % 2 == 0:
            count += 1
    return count

if __name__=='__main__':
    nums = []
    result = find_numbers(nums)
    print(result)
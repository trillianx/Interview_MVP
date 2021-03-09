def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    index = n - 1
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            result[index] = square ** 2
            right -= 1
            index -= 1
        else:
            square = nums[left]
            result[index] = square ** 2
            left += 1
            index -= 1
    return result


if __name__=='__main__':
    nums = [-7, -3, 2, 3, 11]
    result = sortedSquares(nums)
    print(result)
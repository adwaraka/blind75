# Given an array of n distinct integers from 0 to n, one number is missing. Return that missing number.
def missingNumber(nums: list) -> int:
    expectedSum, actualSum = 0, 0
    N = len(nums)
    expectedSum = (N+1)*N//2
    for num in nums:
        actualSum+=num
    return (expectedSum - actualSum)

print(missingNumber([1, 0, 3]))
print(missingNumber([2, 0]))
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

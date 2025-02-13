# Find the smallest missing positive integer from an unsorted integer array
def firstMissingPositive(nums):
    numsLength = len(nums)

    def swap(index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]

    # IMPORTANT: Ensure that every index has the correct value
    # nums[0] = 1, nums[1] = 2; so nums[i] != nums[nums[i] - 1]
    for i in range(numsLength):
        # we have constantly keep doing it so use while
        while nums[i] >= 1 and nums[i] <= numsLength and nums[i] != nums[nums[i] - 1]:
                swap(i, nums[i]-1)

    # there will be one index where the index[x] == x+1
    # condition will fail. That is the result.
    for i in range(numsLength):
        if nums[i] != i + 1:
            return i + 1

    # all numbers are present; return len of nums + 1
    return numsLength + 1

print(firstMissingPositive([3, 4, 5, -1, 1]))
print(firstMissingPositive([3, 4, 5, 2, 1]))
print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([2, 2]))

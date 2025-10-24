"""
https://leetcode.com/problems/contiguous-array/
"""
def findMaxLength(arr: list) -> int:
    result = 0
    countIndex = {0: -1}  # count: index of array
    count = 0
    for index, val in enumerate(arr):
        if val == 0:
            count-=1
        else:
            count+=1

        if count in countIndex.keys():
            diff = index - countIndex[count]
            result = max(result, diff)
        else:
            countIndex[count] = index
    # print(countIndex)
    return result

print(findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0]))
print(findMaxLength([0, 1, 0]))
print(findMaxLength([0, 1]))

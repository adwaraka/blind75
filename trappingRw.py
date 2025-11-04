# https://leetcode.com/problems/trapping-rain-water/
# https://www.enjoyalgorithms.com/blog/trapping-rain-water

# Big O(N) but uses extra storage
def trappingRw(heights: list) -> int:
    n = len(heights)
    if n <= 2:
        return 0

    maxResult = 0
    leftMaxArray, rightMaxArray = [0]*n, [0]*n

    # given an index, what is the maximum value on the left
    leftMaxArray[0] = heights[0]  # first value
    for i in range(1, n):         # ignore the left most
        leftMaxArray[i] = max(leftMaxArray[i - 1], heights[i])

    # given an index, what is the maximum value on the right
    rightMaxArray[n-1] = heights[n-1]  # last value
    for j in range(n - 2, -1, -1):     # ignore the right most
        rightMaxArray[j] = max(rightMaxArray[j + 1], heights[j])

    # to calculate maximum captured water
    for i in range(n):
        maxResult = maxResult + min(leftMaxArray[i], rightMaxArray[i]) - heights[i]

    return maxResult


# https://codewitharyan.com/tech-blogs/trapping-rain-water
# for two pointer solution
def trappingRwTwoPtr(heights: list) ->int:
    left, right, result = 0, len(heights) - 1, 0
    leftMax, rightMax = 0, 0

    while left <= right:
        leftMax = max(leftMax, heights[left])
        rightMax = max(rightMax, heights[right])

        if leftMax < rightMax:
            # left is less than right so look at left
            # this will influence the max height since
            # left maximum cannot be exceeded by water
            result += leftMax - heights[left]
            left+=1
        else:
            result += rightMax - heights[right]
            right-=1

    return result

heights = [1, 0, 2, 1, 0, 1, 2, 1, 2, 1]
print(trappingRw(heights))

heights = [1, 0, 2, 1, 0, 1, 2, 1, 2, 1]
print(trappingRwTwoPtr(heights))

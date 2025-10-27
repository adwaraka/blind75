# https://leetcode.com/problems/trapping-rain-water/
# https://www.enjoyalgorithms.com/blog/trapping-rain-water

# using leftMax and rightMax array coz 2-ptr is hard!!
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

heights = [1, 0, 2, 1, 0, 1, 2, 1, 2, 1]
print(trappingRw(heights))
"""
Given an array of integers heights representing the histogram's 
bar height where the width of each bar is 1, return the area of 
the largest rectangle in the histogram.

Reference:- https://leetcode.com/problems/largest-rectangle-in-
histogram/solutions/6996889/optimal-easy-clear-python-solution-
explanation-muhammed-shafaque/

"""
def largestRectangleArea(heights: list) -> int:
    largestArea = 0
    stack = []
    for index, height in enumerate(heights):
        print()
        print(f"Current {index}, {height}")
        start = index

        # As long as the current height in the for-loop is shorter 
        # than the last stacked height, we keep popping.
        # NOTE: stack[-1][1] is second item of the last element in stack
        while stack and stack[-1][1] > height:
            poppedIndex, poppedheight = stack.pop()
            print(f"Popped {poppedIndex}, {poppedheight}")
            largestArea = max(largestArea, (index - poppedIndex) * poppedheight)
            start = poppedIndex

        # add the current index and height if height is greater than the last
        # element in the stack
        print(f"Pushed {index}, {height}")
        stack.append([index, height])

    # clean out the remaining heights.
    print()
    for index, height in stack:
        # Area will be calcuated from the index till the end of the histogram
        print(f"Remaining {index}, {height}")
        largestArea = max(largestArea, height * (len(heights) - index))

    return largestArea

heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))
def maxArea(height: list[int]) -> int:
    maxArea = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # for the current ptrs, what is the area
        currentArea = (right - left) * min(height[left], height[right])
        maxArea = max(maxArea, currentArea)

        if height[left] < height[right]:
            # left height is less so move it to see if anything is higher
            left += 1
        else:
            right -= 1
    
    return maxArea

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
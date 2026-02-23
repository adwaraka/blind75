def canJump(nums: list) -> int:
    if nums is None or []:
        return 0

    n = len(nums)
    goal = n - 1
    for i in range(n - 1, -1, -1):
        # current index plus whatever the value at the index is
        if i + nums[i] >= goal:
            goal = i
            print(f"Current goal: {goal}")

    if goal == 0:
        return True
    else:
        return False

nums = [2, 3, 1, 1, 4]
print(canJump(nums))

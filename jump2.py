# What are the minimum jumps required to hit the end?
# farthest you can go; reach = max(reach, nums[i])

def minJumps(nums: list) -> int:
    # result is number of jumps
    # reach is the maximum we can jump so far
    # last indicates the maximum reachable index
    result, reach, last = 0, 0, 0
    for i in range(len(nums)-1):
        reach = max(reach, i + nums[i])
        if i == last:
            last = reach
            result+=1
    return result

nums = [2, 3, 1, 1, 4]
print(minJumps(nums))

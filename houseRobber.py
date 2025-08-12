"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security systems connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each
house, return the maximum amount of money you can rob tonight without
alerting the police.
"""

def rob(nums: list[int]) -> int:
    # bag[0] is the amount of money stolen if earlier house had been skipped
    # bag[1] is the maximum of bag[0] and robbing the previous house
    bag = (0, 0)
    for money in nums:
        print(f"Before House {money} {bag}")
        bag = (bag[1], max(bag[1], money + bag[0]))
        print(f"After House {money} {bag}")
        print()
    return bag[1]

print(rob([2, 7, 9, 3, 1]))

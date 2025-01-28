# does array contain duplicates
def containsDuplicate(nums: list):
    map = {}
    for i in nums:
        if i in map.keys():
            return True
        else:
            map[i] = 0
    return False

nums = [4, 2, 1, 3]
print(containsDuplicate(nums))
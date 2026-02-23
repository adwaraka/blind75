# wood cutting
# https://leetcode.com/discuss/post/354854/facebook-phone-screen-cut-wood-by-sithis-d9w0/
# the first comment is the best explanation

def isValid(cutLength: int, wood: list, k: int) -> bool:
    count = 0
    for i in wood:
        if i < cutLength:
            return False
        else:
            count+=i//cutLength
    return count >= k

def cutWood(wood: list, k: int) -> int:
    result = 0
    left, right = 1 , max(wood)  # least that can be cut; and max
    while left < right:
    	# the average of the height is the starting point
        middle = (left + right)//2
        if isValid(middle, wood, k):
            result = middle
            left = middle+1
        else:
            right = middle
    return result

wood = [232, 124, 456]
k = 7
print(cutWood(wood, k))

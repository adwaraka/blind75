# find the number of times the array has been rotated.
# also for find the minimum in the rotated array

def minRotatedArray(arr: list):
    left, right = 0, len(arr) - 1

    while left < right:  # only less; NOT less than equal
        mid = (left + right) >> 1
        # print(left, right)
        if arr[right] <= arr[mid]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left], left
        

arr = [8, 9, -10, 0, 1, 2, 3, 7]
print(minRotatedArray(arr))

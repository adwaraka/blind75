def squaresSorted(arr: list) -> list:
    left, right = 0, len(arr) - 1
    results = []
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            results.append(arr[left]*arr[left])
            left+=1
        else:
            results.append(arr[right]*arr[right])
            right-=1
    return results[::-1]

print(squaresSorted([-11, -4, -1, 0, 4, 7]))
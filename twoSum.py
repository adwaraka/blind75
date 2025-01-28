# sum of two values in array == target exists?
def twoSum(arr: list, target: int):
    indexMap, res = {}, []
    for index, val in enumerate(arr):
        diff = target - val
        # print(diff)
        if diff not in indexMap.keys():
            indexMap[val] = index
        else:
            res.append(indexMap[diff])
            res.append(index)
        # print(indexMap)
    return res

arr = [2, 1, 5, 3]
target = 5
print(twoSum(arr, target))

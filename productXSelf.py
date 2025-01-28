# Return product for all except itself
def productXSelf(arr: list):
    result = [1] * len(arr)
    leftProduct, rightProduct = 1, 1

    for i in range(len(arr)):
        result[i] = leftProduct
        leftProduct *= arr[i]
    # print(result)

    rightProduct = 1
    for i in range(len(arr) - 1, -1, -1):
        # print(result[i], rightProduct)
        result[i] *= rightProduct
        rightProduct *= arr[i]

    return result

arr = [10, 3, 5, 6, 2]
print(productXSelf(arr))

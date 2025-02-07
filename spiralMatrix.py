# print a spiral matrix
def printSpiral(matrix):
    res = []
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        # one row is done; reduce top by one
        top+=1

        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        # one column is done; so from right side by 1
        right-=1

        if top <= bottom:
            # move from right -> left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom-=1

        if left <= right:
            # move from bottom to top
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left+=1

    return res

matrix = [
    [11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [31, 32, 33, 34, 35, 36],
    [41, 42, 43, 44, 45, 46],
    [51, 52, 53, 54, 55, 56],
]
print(printSpiral(matrix))

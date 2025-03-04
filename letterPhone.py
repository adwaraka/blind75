def letterCombinations(digits: str):
    if not digits:
        return []

    ans = ['']
    digitToLetters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    for d in digits:
        temp = []
        for s in ans:
            for c in digitToLetters[int(d)]:
                # print(c)
                temp.append(s + c)
            # print(temp)
        ans = temp
    return ans

# input will be [2, 9]
print(letterCombinations("92"))
print(letterCombinations("87"))

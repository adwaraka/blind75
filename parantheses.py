# generate all parantheses that are valid
def generateParantheses(n: int) -> list:
    res, stack = [], []

    def backtrack(openB: int, closeB: int):
        # number of opened and closed parans = n
        if openB == closeB == n:
            res.append("".join(stack))

        # we require more open parans
        if openB < n:
            stack.append("(")
            backtrack(openB+1, closeB)
            stack.pop()
            # remove the above added paran

        # keep adding close parans till <= open
        if closeB < openB:
            stack.append(")")
            backtrack(openB, closeB+1)
            stack.pop()

    backtrack(0, 0)
    return res

print(generateParantheses(3))
print(generateParantheses(2))
print(generateParantheses(5))

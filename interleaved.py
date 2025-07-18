def isInterleaved(s1: str, s2: str, s3: str) -> bool:
    # do the length of the two strings add up to the 3rd?
    if len(s3) != len(s1) + len(s2):
        return False

    # for s1, s2 and s3; so two pointer is the way to go
    i = 0
    j = 0
    k = 0

    # while s3 is complete
    while k < len(s3):
        if i < len(s1) and s3[k] == s1[i]:
            i += 1
        elif j < len(s2) and s3[k] == s2[j]:
            j += 1
        else:
            return False
        k += 1

    # both the strings have been reached to the end
    return i == len(s1) and j == len(s2)

print(isInterleaved("abc", "xyz", "axbycz"))
print(isInterleaved("abcd", "xyz", "xaybzcd"))

def minDistance(a, b):
    """
    Calculates the minimum number of edits (insertions, deletions, substitutions) 
    needed to transform string b into string a. 
    """
    # Create a DP table
    m = len(a)
    n = len(b)

    """
    Create a 2D table dp of size (m+1) x (n+1) 
    where m is the length of a and n is the length of b.
    Set the first row and column of dp to represent the 
    edit distance when comparing an empty string with b or a respectively.
    """
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    # print(dp)

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n] 

print(minDistance("kitten", "sitting"))
print(minDistance("kitten", "kitten"))

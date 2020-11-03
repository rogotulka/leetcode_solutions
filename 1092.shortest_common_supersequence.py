# Task 1092
# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as
# subsequences. If multiple answers exist, you may return any of them.

# Dynamic programming use LCS(Longest Common Subsequence)
def shortest_common_supersequence(str1: str, str2: str) -> str:
    n = len(str1)
    m = len(str2)

    # matrix of all overlapping
    t = [[0] * (m + 1) for i in range(n + 1)]

    # calculate length of LCS
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    i, j = n, m
    res = []
    while i != 0 and j != 0:
        if str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
            res.append(str1[i])

        elif t[i - 1][j] >= t[i][j - 1]:
            i -= 1
            res.append(str1[i])

        else:
            j -= 1
            res.append(str2[j])

    # add remaining parts of strings
    while i > 0:
        i -= 1
        res.append(str1[i])

    while j > 0:
        j -= 1
        res.append(str2[j])

    # reverse result
    return ''.join(res[::-1])

assert shortest_common_supersequence("abac", "cab"), "cabac"
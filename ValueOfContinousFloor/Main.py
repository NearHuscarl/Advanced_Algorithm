def XuLy(a):
    ln = max(a)
    n = len(a)

    dp = [-1] * (ln + 1)
    dp[0] = 0

    for i in range(1, ln+1):
        dp[i] = dp[i/2] + i

    result = []
    for i in range(n):
        result.append(dp[a[i]])

    return result


a = [6, 10, 4, 5, 7]
print XuLy(a)
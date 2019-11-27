def first_task(k, vals):
    A, dp, prev = range(1, len(vals)), [0], []

    for i in A:
        possible = dp[len(dp) - k:]
        temp = [dp[i - possibility] for possibility in possible]
        dp.append(temp[0] + 1) if len(temp) == 1 else dp.append(min(temp) + 1)


def solve(t, k):
    n = len(t)
    dp = [0] * n
    prev = [0] * n

    # Filling dp
    for i in range(1, n):
        dp[i] = dp[i - 1] + t[i - 1] + 1  
        prev[i] = i - 1

        for j in range(1, k + 1):
            if i - j >= 0 and dp[i - j] + t[i - j] + j <= dp[i]:
                dp[i] = dp[i - j] + t[i - j] + j
                prev[i] = i - j

    # Floors restoration
    n -= 1
    while n != 0:
        n = prev[n]
        print(n + 1)

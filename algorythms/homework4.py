def task_A():
    n = int(input())
    actions = [1, 2, 3]
    dp = [0, 0]
    vals = [1] * n
    n = range(2, n + 1)

    for i in n:
        possible = []
        vals[i - 1] = i - 2
        for action in actions:
            if action == 1:
                possible.append(i - 1)
            elif action == 2 and i % 2 == 0:
                possible.append(i // 2)
            elif action == 3 and i % 3 == 0:
                possible.append(i // 3)
        current_action = [dp[possibility] for possibility in possible]
        if len(current_action) == 1:
            dp.append(current_action[0] + 1)
        else:
            dp.append(min(current_action) + 1)
        # vals[dp[i]] = i  # FIXME set answer restoration

    n = len(vals)
    ans = [n]
    while n != 1:
        if dp[n - 1] + 1 == dp[n]:
            ans.append(n - 1)
            n -= 1
        if n % 2 == 0 and \
                dp[n // 2] + 1 == dp[n]:
            ans.append(n // 2)
            n //= 2
        if n % 3 == 0 and \
                dp[n // 3] + 1 == dp[n]:
            ans.append(n // 3)
            n //= 3

    print(dp[-1])
    print(*ans[::-1])


def task_B():
    n, m = map(int, input().split())
    path = [int(i) for i in input().split()]
    ways = [1]
    ls = 0

    for i in range(1, n):
        if path[i] == 1:
            if len(ways) >= m + 1:
                ls = ls - ways[-(m + 1)] + ways[-1] % 1000000007
            if len(ways) < m + 1:
                ls = ls + ways[-1] % 1000000007
            ways.append(ls)
        if path[i] != 1:
            if len(ways) >= m + 1:
                ls = ls - ways[-(m + 1)] + ways[-1] % 1000000007
            if len(ways) < m + 1:
                ls = ls + ways[-1] % 1000000007
            ways.append(0)

    print(ways[-1] % 1000000007)


# task_A()
# task_B()


# arrr()

for i in enumerate([1, 2, 3], 4):
    print(i)
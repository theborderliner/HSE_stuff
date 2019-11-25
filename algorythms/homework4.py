def task_A():
    n = int(input())
    actions = [1, 2, 3]
    dp = [0, 0]
    vals = [1] * n
    n = range(2, n + 1)

    for i in n:
        possible = []
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
        vals[dp[i]] = i  # FIXME set answer restoration
    print(dp[-1])
    print(*vals[:dp[-1] + 1])


def task_B():
    n, m = map(int, input().split())
    path = list(map(int, input().split()))
    dp = [1]
    s = 0

    for i in range(1, n):
        if path[i] == 1:
            dp.append((dp[-1] - dp[-(m + 1)] + dp[-1] if len(dp) >= m + 1 else 2 * dp[-1]))
        else:
            # s = s - dp[-(m + 1)] + dp[-1] if len(dp) >= m + 1 else s + dp[-1]
            dp.append(0)

    print(dp[-1] % 1000000007)


# task_A()
task_B()

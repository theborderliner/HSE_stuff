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
        vals[dp[i]] = i

    print(dp[-1])
    print(*vals[:dp[-1] + 1])


task_A()

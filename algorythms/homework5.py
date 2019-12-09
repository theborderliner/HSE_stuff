n, C = map(int, input().split())
Ws, Vs, Ns = [], [], []

for i in range(n):
    val = list(map(int, input().split()))
    Ws += [val[0]] * val[-1]
    Vs += [val[1]] * val[-1]


def knapsack_bu(W, V, C):
    n = len(W)
    tbl = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(C + 1):
            tbl[i][j] = tbl[i - 1][j]
            if j >= W[i - 1]:
                tbl[i][j] = max(
                    tbl[i][j],
                    tbl[i - 1][j - W[i - 1]] + V[i - 1]
                )
    return tbl[-1][-1]


print(knapsack_bu(Ws, Vs, C))

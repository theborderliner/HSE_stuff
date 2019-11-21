def first_task(num, vals):
    A = range(1, num)
    dp = [0]
    prev = []

    for i in A:
        possible = [coin for coin in vals if coin <= i]
        temp = [dp[i - possibility] for possibility in possible ]
        if len(temp) == 1:
            dp.append(temp[0] + 1)
        else:
            dp.append(min(temp) + 1)



def third_task():
    arr = list(map(int, input().split()))

    delete = []
    new_arr = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            new_arr.append(arr[i])
        else:
            delete.append(i)

    print(new_arr)


def third_task_n2(arr):
    inv = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            inv += 1

    if inv != 0:
        return third_task_n2(arr[:-1])
    else:
        return arr

# third_task_n2([1, 1, 3, 2, 5, 1, 7])
# third_task()
first_task(26, [1, 3, 7, 8])

# '''
#     бинарным поиском находим место, на которое в массиве vals должен встать
#     текущий num, обозначим это место за k.
#     дальше запускаем рекурсию от num - vals[k] и num - vals[k - 1]
#     O(n*log(n))
# '''

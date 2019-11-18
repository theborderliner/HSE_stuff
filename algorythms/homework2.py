from collections import deque
from queue import Queue


def A():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    res_arr = [0] * (n - k + 1)
    local_sum = 0

    for j in range(k):
        sign = (-1) ** j
        res_arr[0] += sign * (j + 1) * arr[j]
        local_sum += sign * arr[j]

    for i in range(1, n - k + 1):
        sign = (-1) ** (k + 1)
        res_arr[i] = -res_arr[i - 1] + local_sum + sign * k * arr[i + k - 1]
        local_sum = arr[i - 1] + sign * arr[i + k - 1] - local_sum

    print(*res_arr)


def B():
    n, m, k = map(int, input().split())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))

    def append_and_sort(list1, list2):
        res = []
        i, j = 0, 0

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1

        res = res + list1[i:] + list2[j:]
        return res

    arr1 = append_and_sort(arr1, arr2)
    arr2 = append_and_sort(arr1, arr3)

    print(*arr2)


def C():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    pointer1 = 0
    pointer2 = len(arr) - 1
    flag = False

    while pointer2 > pointer1:
        if arr[pointer1] + arr[pointer2] > k:
            pointer2 -= 1
        elif arr[pointer1] + arr[pointer2] < k:
            pointer1 += 1
        else:
            print("YES")
            flag = True
            break

    if not flag:
        print("NO")


def D():
    requests = int(input())

    elems = Queue()
    middles = deque()

    elems_len = middles_len = 0

    for i in range(requests):
        operations = input().split()

        if operations[0] == '+':
            middles.append(int(operations[1]))
            middles_len += 1
        elif operations[0] == '*':
            middles.appendleft(int(operations[1]))
            middles_len += 1
        else:
            print(elems.get())
            elems_len -= 1

        if elems_len < middles_len:
            elems.put(middles.popleft())
            elems_len += 1
            middles_len -= 1

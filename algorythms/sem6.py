

def my_missed_elem(arr):
    def mid(arr):
        left = 0
        right = len(arr) - 1
        mid = arr[(right - left) // 2]
        return mid

    n = len(arr)
    arr1 = arr[: n // 2]
    arr2 = arr[n // 2:]
    sum = arr[0] + arr[-1]
    flag = True
    prev = [-1] * 2
    iterr = 0

    while flag:
        mid1 = mid(arr1)
        mid2 = mid(arr2)
        prev[iterr % 2] = mid1 + mid2
        if mid1 + mid2 < sum:
            arr2 = arr2[len(arr2) // 2:]
        else:
            arr1 = arr1[: len(arr1) // 2]
        if prev[-1] != -1:
            if prev[1] - prev[0] == 2:
                print(mid1, mid2)
            else:
                prev = [-1] * 2
        iterr += 1


# my_missed_elem([0, 1, 2, 3, 4, 6, 7])

def bsearch(arr, l, r, num):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            return bsearch(arr, l, mid - 1, num)
        else:
            return bsearch(arr, mid + 1, r, num)
    else:
        return -1

def task3(arr, t):
    m = max(arr)
    m_id = arr.index(m) + 1
    arr1 = arr[: m_id]
    arr2 = arr[m_id :]
    f1 = bsearch(arr1, 0, len(arr1) - 1, t)
    f2 = bsearch(arr2, 0, len(arr2) - 1, t)
    return f1 if f1 >= 0 else f2 if f2 < 0 else f2 + len(arr1)


def task4(arr):
    pass



print(task3([9,12,13,1,3,5,6,8], 2))



n, m, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))


def appendAndSort(list1, list2):
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


arr1 = appendAndSort(arr1, arr2)
arr2 = appendAndSort(arr1, arr3)

print(*arr2)

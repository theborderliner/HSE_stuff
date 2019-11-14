n, m, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))


def QuickSortPos(a, left, right):
    i = left
    j = right - 1
    while True:  # чтобы поставить разделяющий элемент на свое место
        while a[i] < a[right]:
            i += 1
        while a[j] > a[right] and j > left:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[right], a[i] = a[i], a[right]
    return i

newArr =arr1 + arr2 + arr3

print(QuickSortPos(newArr, 0, len(newArr)))

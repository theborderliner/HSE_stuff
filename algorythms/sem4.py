def first_task():
    iterations = 0
    def recursion(num, iteraions):
        if num <= 0:
            return iteraions


        return min(recursion(num - 8, iteraions + 1), recursion(num - 7, iteraions + 1))

    res = recursion(26, 0)

def third_task():
    arr = list(map(int, input().split()))

    delete = []
    new_arr = [arr[0]]
    local_max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1] and arr[i] >= local_max:
            local_max = arr[i]
            new_arr.append(arr[i])
        else:
            delete.append(i)


    print(new_arr)

first_task()
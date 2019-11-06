from collections import deque

n, k = map(int, input().split())
input_data = list(map(int, input().split()))
left = 0
right = left + k - 1

for i in range(len(input_data)):
    my_set = set(input_data[left:right + 1])
    if len(my_set) < k:
        left += 1
        right += 1
    elif len(my_set) == k:
        print(left, right)

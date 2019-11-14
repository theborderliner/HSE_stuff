def mots(etalon, lengthes):
    l = 0
    r = len(lengthes) - 1
    amount = 0
    while r >= l:
        curr_len = etalon - lengthes[r]
        while curr_len >= lengthes[l] and r >= l:
            curr_len -= lengthes[l]
            l += 1
        amount += 1
        r -= 1
    return amount

amount = 0

def motsR(etalon, lengthes, count = 0):
    global amount
    amount += count
    if len(lengthes) == 0:
        return 0
    l = 0
    r = len(lengthes) - 1
    rest = etalon - lengthes[0]
    if rest >= lengthes[r]:
        motsR(rest, lengthes[:-1])
    else:
        return motsR(etalon, lengthes[1:], 1)




# print(mots(9, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7]))
print(motsR(10, [8, 7, 3]))

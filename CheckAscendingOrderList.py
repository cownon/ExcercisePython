a = list(map(int, input().strip().split(', ')))

def CheckAscendingOrderList(a):
    if a[1] < a[0]:
        return False
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True

if CheckAscendingOrderList(a):
    print('True', end = '')
else:
    print('False', end = '')
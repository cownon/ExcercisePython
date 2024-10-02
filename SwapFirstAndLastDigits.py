import copy

a = int(input())

def SwapFirstAndLastDigits(a):
    b = abs(copy.deepcopy(a))
    tmpList = []
    res = 0

    while(b != 0):
        tmpList.append(b%10)
        b = b // 10
    tmpList.reverse()
    tmpList[0], tmpList[len(tmpList) - 1] = tmpList[len(tmpList) - 1], tmpList[0]

    for i in range(0, len(tmpList)):
        res = res*10 + tmpList[i]

    return res

if (a >= 0):
    print(SwapFirstAndLastDigits(a), end = '')
else:
    print(-SwapFirstAndLastDigits(a), end = '')

s = str(input())

def CheckLength(s):
    if len(s) >= 10:
        return True
    return False

def CheckLetterAndDigit(s):
    for i in s:
        if i not in "abcdefghijklmnopqrstuvwxyz" and i not in "0123456789":
            return False
    return True

def CheckLeastTwoDigits(s):
    countDigit = 0
    for i in s:
        if i in "0123456789":
            countDigit += 1
    if countDigit >= 2:
        return True
    return False

if CheckLength(s) and CheckLeastTwoDigits(s) and CheckLetterAndDigit(s):
    print('True', end = '')
else:
    print('False', end = '')
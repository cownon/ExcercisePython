a = list(map(str, input().strip().split(' ')))
s = a[0]
st = a[1]

def CheckAnagram(s, st):
    for i in range(0, 26):
        if checkS[i] != checkSt[i]:
            return False
    return True

checkS = [i for i in range(0, 26)]
checkSt = [i for i in range(0, 26)]

for i in range(len(s)):
    tmp = int(ord(s[i]) - ord('a'))
    checkS[tmp] += 1

for i in st:
    checkSt[ord(i) - ord('a')] += 1

if CheckAnagram(s, st):
    print('True', end = '')
else:
    print('False', end = '')
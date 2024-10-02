a = list(map(int, input().strip().split(', ')))

res = dict.fromkeys(a)
countRes = []

for i in res:
    countRes.append(a.count(i))

res = tuple(res)
countRes = tuple(countRes)

print(res, end = ' ')
print(countRes, end = '')
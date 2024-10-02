a = int(input())

b = []

while (a != 0):
    b.append(a%10)
    a = a//10

b.reverse()

for i in range(len(b)):
    if i != len(b) - 1:
        print(b[i], end = ' ')
    print(b[i], end = '')
a = list(map(int, input().strip().split(', ')))

def CheckUniqueElements():
    for i in a:
        if a.count(i) > 1:
            return False
    return True

if CheckUniqueElements():
    print('True', end = '')
else:
    print('False', end = '')

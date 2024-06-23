n = int(input())
l1 = list(map(int,input().split()))
m = int(input())
l2 = list(map(int,input().split()))
d = {}

for i in l2:
    d[i] = 0

for i in l1:
    try:
        d[i] += 1
    except:
        pass

for i in d.values():
    print(i, end=' ')
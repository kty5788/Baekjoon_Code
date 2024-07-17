import sys
n = int(sys.stdin.readline())
S = set()
for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'add':
        S.add(a[1])
    elif a[0] == 'check':
        if a[1] in S:
            print(1)
        else:
            print(0)
    elif a[0] == 'remove':
        if a[1] in S:
            S.remove(a[1])
    elif a[0] == 'toggle':
        try:
            S.remove(a[1])
        except:
            S.add(a[1])
    elif a[0] == 'all':
        S = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif a[0] == 'empty':
        S.clear()

import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    l = []
    l.append((a+b)**2 + c**2)
    l.append((b+c)**2 + a**2)
    l.append((a+c)**2 + b**2)

    print(min(l))
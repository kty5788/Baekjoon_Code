import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int,input().split()))

res = 0

for i in range(1,len(h)):
    res += abs(h[i]-h[i-1])

res += n*2 + sum(h)*2 + h[0] + h[-1]

print(res)
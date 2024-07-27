import sys
input = sys.stdin.readline

n,k = map(int,input().split())
kinder = list(map(int,input().split()))
height_diff = [kinder[i]-kinder[i-1] for i in range(1,n)]

height_diff.sort()

for i in range(k-1):
    height_diff.pop()

print(sum(height_diff))
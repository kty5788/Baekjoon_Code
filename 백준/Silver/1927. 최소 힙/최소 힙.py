import sys
input = sys.stdin.readline

import heapq
l = []

n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if not l:
            print(0)
        else:
            print(heapq.heappop(l))
    else:
        heapq.heappush(l,x)
import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            asd = heapq.heappop(heap)
            print(-asd)
        else:
            print(0)
    else:
        heapq.heappush(heap,-x)
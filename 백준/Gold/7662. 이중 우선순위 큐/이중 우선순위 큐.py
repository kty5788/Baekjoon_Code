import heapq
import sys

t = int(sys.stdin.readline())

for i in range(t):
    max_heap = []
    min_heap = []
    k = int(sys.stdin.readline())
    overlap = [False] * k

    for j in range(k):
        cmd,num = sys.stdin.readline().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(min_heap,(num,j))
            heapq.heappush(max_heap,(-num,j))
            overlap[j] = True
        else:
            if num == -1:
                if min_heap:
                    overlap[heapq.heappop(min_heap)[1]] = False
            else:
                if min_heap:
                    overlap[heapq.heappop(max_heap)[1]] = False
            
            while min_heap and overlap[min_heap[0][1]] == False:
                heapq.heappop(min_heap)
            while max_heap and overlap[max_heap[0][1]] == False:
                heapq.heappop(max_heap)
    
    if len(min_heap) == 0:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])
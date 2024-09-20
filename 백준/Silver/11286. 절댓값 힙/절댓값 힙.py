import heapq
import sys

n = int(sys.stdin.readline())
positive_heap = [] # 양수는 최소힙, 음수는 최대 힙으로 구현
negative_heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(positive_heap,x)
    elif x < 0:
        heapq.heappush(negative_heap,-x)
    else:
        if not positive_heap and not negative_heap: # 양수힙, 음수힙 모두 pop 했다면
            print(0)
        elif not positive_heap: # 양수힙의 값이 없다면
            print(-heapq.heappop(negative_heap))
        elif not negative_heap: # 음수힙의 값이 없다면
            print(heapq.heappop(positive_heap))
        else: # 모두 값이 있다면
            if positive_heap[0] >= negative_heap[0]: # 절댓값 비교
                print(-heapq.heappop(negative_heap))
            else:
                print(heapq.heappop(positive_heap))
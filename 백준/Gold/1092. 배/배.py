import sys
input = sys.stdin.readline

n = int(input())
limit = list(map(int,input().split()))
m = int(input())
box = list(map(int,input().split()))

limit.sort(reverse=True)
box.sort(reverse=True)
cnt = 0

if limit[0] < box[0]:
        print(-1)
        exit()
else:
    while box:
        for i in range(len(limit)):
            for j in range(len(box)):
                if limit[i] >= box[j]:
                    del box[j]
                    break
        cnt += 1

print(cnt)
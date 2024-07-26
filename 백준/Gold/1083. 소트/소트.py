import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
s = int(input())

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if s > 0:
            if l[j] == max(l[i+1:i+1+s]) and l[i] < max(l[i+1:i+1+s]):
                #print(l[i],l[j], l,l[i+1:i+1+s])
                index = j
                while index != i and s > 0:
                    l[index],l[index-1] = l[index-1],l[index]
                    index -= 1
                    s -= 1

print(*l)
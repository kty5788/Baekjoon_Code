l = [False,False] + [True for i in range(2,1000000+1)]
def era(n,l):
    for i in range(2,int(n**0.5)+1):
        j = 2
        while i*j <= n:
            l[i*j] = False
            j += 1

era(1000000,l)

t = int(input())
for i in range(t):
    n = int(input())
    
    cnt = 0
    for i in range(2,n//2+1):
        if l[i] and l[n-i]:
            cnt += 1
    print(cnt)
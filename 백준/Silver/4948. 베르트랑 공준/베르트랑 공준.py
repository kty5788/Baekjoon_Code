l = [False,False] + [True for i in range(2,246912+1)]
def era(n,l):
    for i in range(2,int(n**0.5)+1):
        j = 2
        while i*j <= n:
            l[i*j] = False
            j += 1

era(246912,l)
while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt = 0
        for i in range(n+1,2*n+1):
            if l[i]:
                cnt += 1
        print(cnt)
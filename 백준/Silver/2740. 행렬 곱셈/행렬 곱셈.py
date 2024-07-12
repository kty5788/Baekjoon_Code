n,m = map(int,input().split())
l1 = []
for i in range(n):
    l1.append(list(map(int,input().split())))

m,k = map(int,input().split())
l2 = []
for i in range(m):
    l2.append(list(map(int,input().split())))


for i in range(n):
    for j in range(k):
        numb = 0
        for q in range(m):
            numb += l1[i][q] * l2[q][j]
        print(numb, end=' ')
    print('')
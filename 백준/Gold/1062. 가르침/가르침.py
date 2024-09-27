import itertools

n,k = map(int,input().split())
l = []
alpha_set = set()
ans = 0
for i in range(n):
    x = set(list(input()))-{'a','n','t','i','c'}
    alpha_set = alpha_set.union(x)
    l.append(x)

if k < 5:
    print(0)
else:
    for i in itertools.combinations(alpha_set,min(k-5,len(alpha_set))):
        res = 0
        i = set(i)
        for j in l:
            if i&j == j:
                res += 1
        if res > ans:
            ans = res
    print(ans)
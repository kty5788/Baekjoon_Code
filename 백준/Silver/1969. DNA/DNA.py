n,m = map(int,input().split())
l = [list(input()) for _ in range(n)]
ans = []
cnt = 0

for i in range(m):
    alphabet_list = []
    for j in range(n):
        alphabet_list.append(l[j][i])
    alphabet_list.sort()
    most_frequent = max(alphabet_list, key=alphabet_list.count)
    ans.append(most_frequent)
    for j in range(n):
        if most_frequent != l[j][i]:
            cnt += 1


print(*ans,sep='')
print(cnt)

string,n = list(input().split())
notation = []
ans = 0
for i in string:
    if i.isdigit():
        notation.append(int(i))
    else:
        notation.append(ord(i)-55)

cnt = 0
for i in notation[::-1]:
    ans += i * (int(n) ** cnt)
    cnt += 1

print(ans)
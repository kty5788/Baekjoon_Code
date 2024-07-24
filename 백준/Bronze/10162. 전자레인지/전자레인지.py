t = int(input())
count = [0,0,0]
while t >= 10:
    if t >= 300:
        count[0] += t//300
        t %= 300
    elif t >= 60:
        count[1] += t//60
        t %= 60
    elif t >= 10:
        count[2] += t//10
        t %= 10

if t != 0:
    print(-1)
else:
    print(*count)
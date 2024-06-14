t = int(input())
for i in range(t):
    li = []
    s = set()
    n = int(input())
    index = 1
    for j in range(n):
        li.append(int(input()))

    while True:
        for studentid in li:
            s.add(studentid%index)
        if len(s) == len(li):
            print(index)
            break
        else:
            index += 1
            s.clear()
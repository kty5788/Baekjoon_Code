n = int(input())
pn = 'IO' * n + 'I'
s = int(input())
m = input()
index = 0
cnt = 0

for i in range(len(m)):
    if m[i] == pn[index]:
        index += 1
    else:
        if m[i] == 'I':
            index = 1
        else:
            index = 0
    if index == len(pn):
        cnt += 1
        index -= 2
    
print(cnt)

cnt1,cnt2 = 0,0
string = list(input())
for i in range(len(string)):
    if string[i] == '0':
        if i == len(string)-1:
            cnt1 += 1
            break

        if string[i+1] != '0':
            cnt1 += 1


for i in range(len(string)):
    if string[i] == '1':
        if i == len(string)-1:
            cnt2 += 1
            break

        if string[i+1] != '1':
            cnt2 += 1


print(min(cnt1,cnt2))
n,k = map(int,input().split())
two_exp_list = [1,]

while True:
    if two_exp_list[-1]*2 <= n:
        two_exp_list.append(two_exp_list[-1]*2)
    else:
        break

index = 0
while k > 0 and n > 0:
    if two_exp_list[index] <= n and 2*two_exp_list[index] > n:
        if k == 1:
            last_bottle = two_exp_list[index]
        k -= 1
        n -= two_exp_list[index]
        index = 0
    else:
        index += 1

if n > 0:
    print(last_bottle-n)
else:
    print(0)
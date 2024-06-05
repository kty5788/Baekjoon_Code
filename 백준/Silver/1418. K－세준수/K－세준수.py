n = int(input())
k = int(input())
cnt = 0
prime_numb = [False,False] + [True for i in range(2,k+1)]
for i in range(2,int(k**0.5)+1):
    index = 2
    while i*index < len(prime_numb):
        prime_numb[i*index] = False
        index += 1
    
for i in range(1,n+1):
    num = i
    index = 2
    while index < len(prime_numb):
        if prime_numb[index]:
            if num % index == 0:
                num = int(num/index)
            else:
                index += 1
        else:
            index += 1
        
        if num == 1:
            cnt += 1
            break

if cnt == 0:
    print(1)
else:
    print(cnt)
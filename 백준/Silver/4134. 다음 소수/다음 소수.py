t = int(input())
for i in range(t):
    n = int(input())
    while True:
        if n < 2:
            print(2)
            break
        is_prime = True
        for j in range(2,int(n**0.5)+1):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            print(n)
            break
        else:
            n += 1
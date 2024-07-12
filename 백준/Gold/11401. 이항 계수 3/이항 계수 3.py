n,k = map(int,input().split())
p = 1000000007

# 거듭제곱 구하기
def powa(n,k):
    global p
    if k == 1:
        return n
    else:
        x = powa(n,k//2)
        if k % 2 == 0:
            return x*x%p
        else:
            return x*x*n%p

# 팩토리얼 구하기
def fact(n):
    num = 1
    for i in range(2,n+1):
        num = num * i % p
    return num


# 조합 공식 분자, 분모
a = fact(n)
b = fact(n-k)*fact(k)%p

# 페르마의 소정리
ans = a* powa(b,p-2)%p
print(ans)
t = int(input())
for i in range(1,t+1):
    a,b,c = list(map(int,input().split()))
    if 2*max(a,b,c) >= a+b+c:
        print(f"Case #{i}: invalid!")
    elif a == b ==c == a:
        print(f"Case #{i}: equilateral")
    elif a == b or b == c or a == c:
        print(f"Case #{i}: isosceles")
    else:
        print(f"Case #{i}: scalene")


e,s,m = list(map(int,input().split()))
a,b,c = [0,0,0]
year = 0
while True:
    year += 1
    a = a % 15 + 1
    b = b % 28 + 1
    c = c % 19 + 1
    if a == e and b == s and c == m:
        print(year)
        break
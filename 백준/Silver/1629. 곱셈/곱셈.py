a,b,c = map(int,input().split())

def divide_conquer(a,b):
    global c
    if b == 1:
        return a%c
    else:
        x = divide_conquer(a,b//2)
        if b % 2 == 0:
            return x*x%c
        else:
            return x*x*a%c

print(divide_conquer(a,b))
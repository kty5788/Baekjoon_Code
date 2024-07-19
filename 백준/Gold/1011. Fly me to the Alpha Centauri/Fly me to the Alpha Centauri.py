n = int(input())
for i in range(n):
    start,end = map(int,input().split())
    d = end-start
    max_number = int(d**0.5)
    if d**0.5 == max_number:
        print(2*max_number-1)
    else:
        if d - max_number**2 > max_number:
            print(2*max_number+1)
        else:
            print(2*max_number)

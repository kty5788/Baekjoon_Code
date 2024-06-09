index = 1
while True:
    a,b,c = list(map(int,input().split()))
    if a == b == c == 0:
        exit()
    print(f'Triangle #{index}')
    if a == -1:
        a = (c**2 - b**2)**0.5
        if c <= b or c >= a+b:
            print('Impossible.')
        else:
            print(f'a = {a:.3f}')
    elif b == -1:
        b = (c**2 - a**2)**0.5
        if c <= a or c >= a+b:
            print('Impossible.')
        else:
            print(f'b = {b:.3f}')
    elif c == -1:
        c = (a**2 + b**2)**0.5
        print(f'c = {c:.3f}')
    print('')
    index += 1
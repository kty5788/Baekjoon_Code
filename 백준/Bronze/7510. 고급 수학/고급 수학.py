t = int(input())
for i in range(1,t+1):
    a,b,c = list(map(int,input().split()))
    print(f'Scenario #{i}:')
    if a**2 == b**2 + c**2 or a**2 + b**2 == c**2 or b**2 == a**2 + c**2:
        print('yes')
        print('')
    else:
        print('no')
        print('')
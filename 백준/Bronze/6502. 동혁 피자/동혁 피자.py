index = 0
while True:
    index += 1
    try:
        r,w,l = list(map(int,input().split()))
        print(f'Pizza {index} ', end = '')
        if (w**2 + l**2) <= (r*2)**2:
            print('fits on the table.')
        else:
            print('does not fit on the table.')
    except ValueError:
        exit()

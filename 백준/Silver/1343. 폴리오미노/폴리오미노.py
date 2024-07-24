b = input().split('.')
for i in range(len(b)):
    if len(b[i]) % 2 != 0:
        print(-1)
        exit()
    else:
        if len(b[i]) % 4 == 0:
            b[i] = len(b[i])//4 * 'AAAA'
        elif len(b[i]) % 2 == 0:
            b[i] = len(b[i])//4 * 'AAAA' + (len(b[i])%4)//2 * 'BB'

print('.'.join(b))
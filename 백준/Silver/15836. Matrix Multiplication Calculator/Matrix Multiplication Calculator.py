attempt = 1
while True:
    n1,m1,n2,m2 = map(int,input().split())

    if n1 == 0 and n2 == 0 and m1 == 0 and m2 == 0:
        break
    else:
        matrix1 = [list(map(int,input().split())) for _ in range(n1)]
        matrix2 = [list(map(int,input().split())) for _ in range(n2)]
        
        print(f'Case #{attempt}:')
        if n2 != m1:
            print('undefined')
        else:
            for i in range(n1):
                print('| ',end='')
                for j in range(m2):
                    numb = 0
                    for k in range(n2):
                        numb += matrix1[i][k] * matrix2[k][j]
                    print(numb,end=' ')
                print('|')
        attempt += 1
n = int(input())
m = 0
if n <= 2:
    print(0,3,sep='\n')
else:
    for i in range(1,n-1):
        m += (n-1-i)*i

    print(m,3,sep='\n')
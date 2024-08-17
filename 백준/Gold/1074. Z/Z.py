N,r,c = map(int,input().split())
cnt = -1

def divide_n_conquer(row,col,n):
    global cnt
    if n == 0: # 마지막 1칸이 되었을떄
        cnt += 1
        if row == r and col == c:
            print(cnt)
            exit()
    else: # 2 ** n 칸일 떄 분할정복
        # r행 c열이 해당되는 부분만 분할정복
        divide_cntnum = 2**(n-1) * 2**(n-1)
        if r <= row+2**n//2-1 and c <= col+2**n//2-1:
            divide_n_conquer(row, col, n-1)
        elif r <= row+2**n//2-1 and c > col+2**n//2-1:
            cnt += divide_cntnum
            divide_n_conquer(row, col+2**n//2, n-1)
        elif r > row+2**n//2-1 and c <= col+2**n//2-1:
            cnt += divide_cntnum*2
            divide_n_conquer(row+2**n//2, col, n-1)
        else:
            cnt += divide_cntnum*3
            divide_n_conquer(row+2**n//2, col+2**n//2, n-1)

divide_n_conquer(0,0,N)
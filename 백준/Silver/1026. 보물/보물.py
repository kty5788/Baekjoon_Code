n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
    
for i in range(1,len(A)):
    key = A[i]
    j = i-1
    while j > -1 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key

for i in range(1,len(B)):
    key = B[i]
    j = i-1
    while j > -1 and B[j] < key:
        B[j+1] = B[j]
        j -= 1
    B[j+1] = key

cnt = 0
for i in range(len(A)):
    cnt += A[i] * B[i]

print(cnt)
N = int(input())
A = [input().split() for _ in range(N)]
B = [input().split() for _ in range(N)]

AA = [int(''.join(a), 2) for a in A]
BB = [int(''.join(B[r][c] for r in range(N)), 2) for c in range(N)]
cnt = 0

for Ai in AA:
    for Bi in BB:
        if Ai & Bi:
            cnt += 1
print(cnt)
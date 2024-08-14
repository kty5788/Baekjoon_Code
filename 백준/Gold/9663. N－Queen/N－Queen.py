n = int(input())
row = [-1 for i in range(n)]
cnt = 0

def is_duplicate(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return True
    return False


def BruteForce(index):
    global cnt
    if index == n:
        cnt += 1
    else:
        for i in range(n):
            row[index] = i

            if not is_duplicate(index):
                BruteForce(index+1)

BruteForce(0)

print(cnt)
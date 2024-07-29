s1 = list(input())
s2 = list(input())

LCS = [[0 for row in range(len(s1)+1)] for col in range(len(s2)+1)]

for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])

print(max(LCS[-1]))
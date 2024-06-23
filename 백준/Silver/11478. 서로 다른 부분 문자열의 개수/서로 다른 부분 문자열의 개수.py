s = input()
s1 = set()
for i in range(len(s)):
    for j in range(len(s)):
        s1.add(s[i:j+1])

print(len(s1)-1)
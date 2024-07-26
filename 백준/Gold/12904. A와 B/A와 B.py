import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

while len(t) != len(s):
    if t[-1] == 'B':
        t.pop()
        t.reverse()
    elif t[-1] == 'A':
        t.pop()

if s == t:
    print(1)
else:
    print(0)
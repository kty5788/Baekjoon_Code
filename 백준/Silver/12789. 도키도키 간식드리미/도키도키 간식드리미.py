n = int(input())
stack1 = list(map(int,input().split()))
stack1.reverse()
stack2 = []
line = [0,]


waiting_number = 1
while True:
    if not stack1 and not stack2:
        break
    else:
        if stack2:
            if stack2[-1] == waiting_number:
                line.append(stack2.pop())
                waiting_number += 1
                continue
            elif not stack1:
                line.append(stack2.pop())
        
        if stack1:
            if stack1[-1] == waiting_number:
                line.append(stack1.pop())
                waiting_number += 1
                continue

            else:
                stack2.append(stack1.pop())

for i in range(1,n+1):
    if line[i] != i:
        print('Sad')
        exit()

print('Nice')
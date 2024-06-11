t = int(input())
for _ in range(t):
    iserror = False
    isR = False
    func = input()
    num = int(input())
    string = input()
    try:
        li = list(map(int,string[1:-1].split(',')))
    except:
        li = []
    
    for i in func:
        if i == 'R':
            if isR:
                isR = False
            else:
                isR = True
        elif i == 'D':
            if len(li):
                if isR:
                    li.pop()
                else:
                    del li[0]
            else:
                iserror = True
                
    if iserror:
        print('error',end = '')
    else:
        if isR:
            li.reverse()
        for i in str(li):
            if i != ' ':
                print(i, end = '')
    print('')

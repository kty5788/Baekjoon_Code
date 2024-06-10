def cal(x,y,s=0):
    x = float(x)
    y = float(y)
    
    length = (x**2 + y**2)**0.5
    if length <= 3:
        s += 100
    elif length <= 6:
        s += 80
    elif length <= 9:
        s += 60
    elif length <= 12:
        s += 40
    elif length <= 15:
        s += 20
    return s

t = int(input())
for i in range(t):
    count = []
    score1 = 0
    score2 = 0
    asd = list(input().split())
    for i in range(0,len(asd),2):
        if i <= 4:
            score1 += cal(asd[i],asd[i+1])
        else:
            score2 += cal(asd[i],asd[i+1])
        
    print(f'SCORE: {score1} to {score2}, ', end = '')
    if score1 > score2:
        print('PLAYER 1 WINS.')
    elif score1 < score2:
        print('PLAYER 2 WINS.')
    else:
        print('TIE.')
n = int(input())
dice = list(map(int,input().split()))
min_dice_sum = [0,min(dice)]

def cal(dice, exposure):
    if exposure == 2:
        num = 101
        for i in range(len(dice)):
            for j in range(len(dice)):
                if j != i and j != len(dice)-i-1:
                    if dice[i] + dice[j] < num:
                        num = dice[i] + dice[j]
        return num
    
    elif exposure == 3:
        num = 151
        for i in range(len(dice)):
            for j in range(len(dice)):
                for k in range(len(dice)):
                    if j != i and j != len(dice)-i-1 and k != i and k != len(dice)-i-1 and k != j and k != len(dice)-j-1:
                        if dice[i] + dice[j] + dice[k] < num:
                            num = dice[i] + dice[j] + dice[k]
        return num
        
min_dice_sum.append(cal(dice,2)) # 주사위 2개 면이 보일때의 최소 값
min_dice_sum.append(cal(dice,3)) # 주사위 3개 면이 보일때의 최소 값

if n > 1:
    print((n-1)*(4*min_dice_sum[2]+(n-2)*4*min_dice_sum[1]) + (min_dice_sum[3]*4 + (n-2)**2 * min_dice_sum[1] + (n-2)*4*min_dice_sum[2]))
else:
    print(sum(dice)-max(dice))
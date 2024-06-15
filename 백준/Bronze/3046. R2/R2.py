class cal():
    def __init__(self,r1,s):
        self.r2 = 2*s-r1

r1,s = list(map(int,input().split()))
number = cal(r1,s)
print(number.r2)
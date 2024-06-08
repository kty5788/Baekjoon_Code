d,h,v = list(map(int,input().split()))
asd = (d**2 / (h**2 + v**2))**0.5
print(int(h*asd),int(v*asd))
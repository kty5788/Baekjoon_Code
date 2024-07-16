coordinate = []
for i in range(4):
    coordinate.append(list(map(int,input().split())))

distance = 0
distance_list = []

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i != j and j != k and k != i:
                distance += ((coordinate[i][0] - coordinate[0][0])**2 + (coordinate[i][1] - coordinate[0][1])**2)**0.5
                distance += ((coordinate[j][0] - coordinate[i][0])**2 + (coordinate[j][1] - coordinate[i][1])**2)**0.5
                distance += ((coordinate[k][0] - coordinate[j][0])**2 + (coordinate[k][1] - coordinate[j][1])**2)**0.5
                distance_list.append(int(distance))
                distance = 0

print(min(distance_list))
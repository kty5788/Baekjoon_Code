from itertools import combinations

l,c = map(int,input().split())
c_list = list(input().split())
vowel_list = ['a','e','i','o','u']
c_list.sort()

for i in combinations(c_list,l):
    count = 0
    for j in i:
        if j in vowel_list:
            count += 1
    
    if count >= 1 and count <= l-2:
        print(''.join(i))
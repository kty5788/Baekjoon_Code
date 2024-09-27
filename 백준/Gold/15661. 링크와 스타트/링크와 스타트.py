import itertools

n = int(input())
l = []
ans = 100 * (n**2-n)

for i in range(n):
    l.append(list(map(int,input().split())))

people = set(i for i in range(n))
for i in range(n):
    for l_people in itertools.combinations(people,i+1):
        link_team, start_team = 0,0
        s_people = people-set(l_people)
        if len(l_people) != 0:
            for k in itertools.permutations(l_people,2):
                link_team += l[k[0]][k[1]]
        
        if len(s_people) != 0:
            for k in itertools.permutations(s_people,2):
                start_team += l[k[0]][k[1]]
        
        if ans > abs(link_team-start_team):
            ans = abs(link_team-start_team)

print(ans)
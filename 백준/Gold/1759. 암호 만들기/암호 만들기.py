l,c = map(int,input().split())
c_list = list(input().split())
vowel_list = ['a','e','i','o','u']
ans = set()
c_list.sort()

def cal(start,string=''):
    if len(string) == l:
        vowel,conso = 0,0
        for i in string:
            if i in vowel_list:
                vowel += 1
            else:
                conso += 1
        if vowel >= 1 and conso >= 2:
            return ans.add(string)
        else:
            return

    for i in range(start,len(c_list)):
        for j in range(1,len(c_list)):
            cal(i+j,string+c_list[i])

for i in range(len(c_list)):
    cal(i)

ans = list(ans)
ans.sort()

for i in ans:
    print(i)
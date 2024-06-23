def merge_sort(l,left,right):
    if left < right:
        mid = (left+right) // 2

        merge_sort(l,left,mid)
        merge_sort(l,mid+1,right)

        return merge(l,left,right)

def merge(l,left,right):
    mid = (left+right) // 2
    lp,rp = left,mid+1
    tmp= []
    
    while True:
        if lp <= mid and rp <= right:
            if l[lp] <= l[rp]:
                tmp.append(l[lp])
                lp += 1
            else:
                tmp.append(l[rp])
                rp += 1
        elif lp <= mid:
            tmp.append(l[lp])
            lp += 1
        elif rp <= right:
            tmp.append(l[rp])
            rp += 1
        else:
            break
    
    l[left:right+1] = tmp
    return l

n = int(input())
s = list(map(int,input().split()))
l = list(set(s))

merge_sort(l,0,len(l)-1)

d = {}
for i in l:
    d[i] = -1

for i in range(len(l)):
    d[l[i]] = i

for i in s:
    print(d[i], end= ' ')

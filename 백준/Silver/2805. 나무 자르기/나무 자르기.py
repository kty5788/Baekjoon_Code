n,m = map(int,input().split())
l = list(map(int,input().split()))
l.sort(reverse= True)
left,right = 1, sum(l)

while left <= right:
    mid = (left+right)//2

    m_tree = 0
    for i in l:
        if i - mid > 0:
            m_tree += i - mid
        else:
            break
    
    if m_tree < m:
        right = mid - 1
    elif m_tree >= m:
        left = mid + 1

print(right)
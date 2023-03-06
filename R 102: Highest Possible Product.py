n=int(input())
a=list(map(int,input().split()))
for i in range(3):
    mind=i
    for j in range(i+1,n):
        if a[j]>a[mind]:mind=j
    a[i],a[mind]=a[mind],a[i]
print(a[0]*a[1]*a[2])

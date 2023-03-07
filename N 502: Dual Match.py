def bs(a,k):
    l,h=0,len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]==k: return 1
        elif a[m]>k:h=m-1
        else: l=m+1
    return 0
n=int(input())
a=list(map(int,input().split()))
k=int(input())
a.sort()
c=0
for i in a:
    if bs(a,k-i):c+=1
print(c)

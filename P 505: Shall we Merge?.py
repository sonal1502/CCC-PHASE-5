def merge(a,l,m,h):
    b=[];i=l;j=m;c=0
    while i<m and j<=h:
        if a[i]<a[j]:b.append(a[i]);i+=1
        else:c+=(m-i);b.append(a[j]);j+=1
    while i<m:b.append(a[i]);i+=1
    while j<=h:b.append(a[j]);j+=1
    k=0
    for x in range(l,h+1):a[x]=b[k];k+=1
    return c

def mergesort(a,l,h):
    c=0
    if l<h:
        m=(l+h)//2
        c+=mergesort(a,l,m)
        c+=mergesort(a,m+1,h)
        c+=merge(a,l,m+1,h)
    return c

n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
print(mergesort(a,0,n-1))

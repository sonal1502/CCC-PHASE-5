n,m=map(int, input().split())
a=list(map(int,input().split()))
a.sort()
gift=[]
while len(gift)<m:
    gift.extend(list(map(int,input().split())))
j=0
for i in gift: 
    sum=c=0
    while sum<i:
        if j==n:break
        sum+=a[j];c+=1;j+=1
    else: print(c,sum)
    if sum<i:print(-1,-1)

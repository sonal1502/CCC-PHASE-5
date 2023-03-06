n=int(input())
a=list(map(int,input().split()))
pucca=garu=f=i=0;j=n-1
while i<=j:
    if f==0:
        if a[i]>=a[j]: pucca+=a[i]; i+=1
        else: pucca +=a[j];j-=1
        f=1
    else: 
        if a[i]>=a[j]: garu+=a[i];i+=1
        else: garu+=a[j];j-=1
        f=0
print(pucca,garu)

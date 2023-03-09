a=input()
b=input()
m1=0;n=len(a);m=len(b)
dp=[[0]*(m+1) for i in range (n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1]:dp[i][j]=dp[i-1][j-1]+1
        m1=max(m1,dp[i][j])
        print(dp[i][j],end=' ')
    print()
print(m1)


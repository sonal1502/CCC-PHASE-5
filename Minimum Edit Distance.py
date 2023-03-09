a=input()
b=input()
m1=0;n=len(a);m=len(b)
dp=[[0]*(m+1) for i in range (n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==0: dp[i][j]=j
        elif j==0: dp[i][j]=i
        elif a[i-1]==b[j-1]:dp[i][j]=dp[i-1][j-1]+1
        else: dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        m1=max(m1,dp[i][j])
        print(dp[i][j],end=' ')
    print()
print(m1)

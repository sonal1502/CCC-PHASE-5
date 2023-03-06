n=int(input())
mice=list(map(int,input().split()))
holes=list(map(int,input().split()))
mice.sort()
holes.sort()
m=0
for i in range(n):
    m=max(m,abs(mice[i]-holes[i]))
print(m)

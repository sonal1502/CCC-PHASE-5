from operator import itemgetter 
n=int(input())
emp=[]
for _ in range(n):
    name,sal=input().split()
    sal=int(sal)
    emp.append([name,sal])
emp.sort(key=itemgetter(1,0))
for i in emp:
    print(*i)

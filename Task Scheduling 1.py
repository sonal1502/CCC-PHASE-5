for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    p=list(map(int,input().split()))
    m=0;job=[]
    for i in range(n):
        m=max(m,d[i])
        job.append([p[i],d[i]])
    job.sort(reverse=True)
    slot=[0]*(m+1)
    for i in range(n):
        if slot[job[i][1]]==0:slot[job[i][1]]=job[i][0]
        else: 
            for j in range(job[i][1]-1,0,-1):
                if slot[j]==0:slot[j]=job[i][0];break
    print(sum(slot))

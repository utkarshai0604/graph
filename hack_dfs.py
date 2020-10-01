from collections import defaultdict

count=0

def dfs(v , visited):
    global count
    count+=1
    visited[v]=True
    for i in graph[v]:
        if(visited[i]==False):
            dfs(i, visited)

for _ in range(int(input())):
    graph=defaultdict(list)
    n,m,cl,cr=map(int, input().split())
    c=0
    se=set()
    ki=0
    for _ in range(m):
            u,v=map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
            se.add(u)
            se.add(v)
    if(cr>cl):
        print(n*cl)
        continue
    else:    
        ki=n-len(se)
        length=len(graph)
        visited=[False]*(n+1)
        sum=0
        for i in se:
            if(visited[i]==False):
                c+=1
                dfs(i, visited)
                sum+=(count-1)*cr+cl
                count=0
        print(sum+(ki*cl))

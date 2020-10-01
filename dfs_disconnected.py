from collections import defaultdict
count=0
def dfs(v , visited):
    global count
    count+=1
    visited[v]=True
    print(v)
    for i in graph[v]:
        if(visited[i]==False):
            dfs(i, visited)

k=int(input())
c=0
graph=defaultdict(list)
for _ in range(k):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
length=len(graph)
visited=[False]*(length+1)
for i in range(1,length+1):
    if(visited[i]==False):
        c+=1
        dfs(i, visited)
        print(str(count)+"count")
        count=0
#print(count)
print(c)

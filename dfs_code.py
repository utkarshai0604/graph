from collections import defaultdict
count=0
def dfs(v , visited):
    global count
    count+=1
    visited[v]=True
#    print(v)
    for i in graph[v]:
        if(visited[i]==False):
            dfs(i, visited)

n,k=map(int, (input().split()))
c=0
a=[]
graph=defaultdict(list)
for _ in range(k):
    u,v=map(int, input().split())
    graph[u+1].append(v+1)
    graph[v+1].append(u+1)
length=len(graph)
visited=[False]*(length+1)
for i in range(1,length+1):
    if(visited[i]==False):
        c+=1
        dfs(i, visited)
 #       print(str(count)+"count")
        a.append(count)
        count=0
#print(count)
#print(c)
print(len(a))
print(a)
#a=[7,2,1,4]
s=a[0]*a[1]
s1=a[0]
for i in range(1,len(a)-1):
    s1+=a[i]
    s+=s1*a[i+1]

print(s)


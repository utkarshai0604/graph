import sys
sys.setrecursionlimit(100000)

def isSafe(i,j,visited, a):
    return (i>-1 and j>-1 and j<len(a[0]) and i<len(a) and a[i][j]==1 and visited[i][j]==0)
        

def dfs(i,j,visited, a):
    row=[-1, -1, -1, 0, 0, 1, 1, 1]
    col=[-1, 0, 1, -1, 1, -1, 0, 1]
    visited[i][j]=1
    for k in range(8):
        if(isSafe(i+row[k],j+col[k], visited, a)):
            dfs(i+row[k],j+col[k], visited, a)
            


def findIslands(a,n,m):
    
    visited=[[0 for j in range(m)] for i in range(n)]
    cnt=0
    for i in range(n):
        for j in range(m):
            if(visited[i][j]==0 and a[i][j]==1):
                dfs(i,j,visited, a)
                cnt+=1
                
    return cnt

for _ in range(int(input())):
    n,m=map(int, input().split())
    l=list(map(int, input().split()))
    m=findIslands(l,n,m)
    print(m)

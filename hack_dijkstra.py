from heapq import *
#from itertools import *
from sys import stderr

def main():
    nvert, nedge, setsize = readints()
    vertexhas = []
    for _ in range(nvert):
        nelts, *elts = readints()
        #assert nelts == len(elts)
        vertexhas.append(sum(1<<(elt-1) for elt in elts))
        # a<<b a multiplied by 2 b times  a*(2**b)
        #a>>b  this gives in int// a/(2**b) this gives in float
    edgelist = [readints() for _ in range(nedge)]
    print(edgelist)
    print(len(edgelist))
    print(len(vertexhas))
    print(vertexhas)
    print(solve(vertexhas, getedges(edgelist, len(vertexhas)), setsize))

def readints():
    return [int(fld) for fld in input().split()]

def getedges(edgelist, nvert):
    edges = [[] for _ in range(nvert)]
    for a, b, cost in edgelist:
        edges[a-1].append((b-1, cost))
        edges[b-1].append((a-1, cost))
    return edges

def solve(vertexhas, edges, setsize):
    costs = getcost(vertexhas, edges, setsize, 0)
    return bestcost(costs[-1])

def getcost(vertexhas, edges, setsize, source):
    costs = [[float('Inf')] * 2**setsize for _ in vertexhas]
    print(costs)
    heapset = [[] for _ in range(2**setsize)]
    print("hello")
    print(heapset[vertexhas[source]])
    heappush(heapset[vertexhas[source]], (0, source))
    for curset, heap in enumerate(heapset):
        while(heap):
            cost, vert = heappop(heap)
            oldcost = costs[vert][curset]
            if cost < oldcost:
                costs[vert][curset] = cost
                for newvert, newcost in edges[vert]:
                   heappush(heapset[curset | vertexhas[newvert]], (cost+newcost, newvert))
    return costs
        
def bestcost(costs):
    costs = list(costs)
    print(costs, file=stderr)
    for i in range(len(costs)-1, -1, -1):
        j = 1
        while j <= i:
            if j & i:
                costs[i-j] = min(costs[i-j], costs[i])
            j <<= 1
    print(costs, file=stderr)
    return min(max(costs[i], costs[~i]) for i in range(len(costs)//2))
   
main()
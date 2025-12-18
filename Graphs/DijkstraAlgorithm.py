# Dijkstra's Algorithm 
# For finding shortest path between two nodes.
from heapq import heappop, heappush


def shortestPath(n, edges, s):
    adjList = []
    for i in range(n):
        adjList.append([])
    
    for edge in edges:
        x = edge[0] -1 
        y = edge[1] -1
        w = edge[2]
        
        adjList[x].append([y,w])
        adjList[y].append([x,w])
    
    heap = [] 
    dist = [float('inf')] * n
    
    s -= 1
    dist[s] = 0
    heappush( heap,( dist[s], s))
    
    while len(heap) > 0:
        d, u = heappop(heap)
        
        for v,w in adjList[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(heap, (dist[v], v))
                
    result = []
    
    for i in range(n):
        if i ==s:
            continue
        elif dist[i] == float('inf'):
            result.append(-1)
        else:
            result.append(dist[i])
    
    return result


n = 6
edges = [[0,1,4],
         [0,2,4],
         [1,2,2],
         [2,3,3],
         [2,4,1],
         [2,5,6],
         [3,5,2],
         [4,5,3]] 
s  = 0

print(shortestPath(n, edges, s))
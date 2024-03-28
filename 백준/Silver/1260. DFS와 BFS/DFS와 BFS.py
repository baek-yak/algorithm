#1260 
from collections import deque

def dfs(start):
    visited[start] = 1
    print(start, end =" ")
    
    for i in adj[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited[start] = 1
    
    while q:
        v = q.popleft()
        print(v, end=" ")
        
        for i in adj[v]:
            if not visited[i]:
                visited[i] = 1    
                q.append(i)

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
    
for i in adj:
    i.sort()
    
#dfs
visited = [0] * (N+1)
dfs(V)

print()

#bfs
visited = [0] * (N+1)
bfs(V)

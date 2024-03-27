from heapq import heappop, heappush

def solution(N, road, K):
    ans = 0
    v = [1e9] * (N+1)
    adj = [[] for _ in range(N+1)]
    
    for s, e, w in road:
        adj[s].append((e,w))
        adj[e].append((s,w))
    
    v[1] = 0
    h = [(0,1)]
    
    while h:
        time, now = heappop(h)
        
        if v[now] < time:
            continue
        
        for next_c, next_time in adj[now]:
            d = time + next_time
            if v[next_c] > d:
                v[next_c] = d
                heappush(h, (d,next_c))
            
    for d in v[1:]:
        if d <= K:
            ans += 1
    
    return ans
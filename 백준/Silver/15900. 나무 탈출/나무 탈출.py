'''
백준 15900 나무 탈출

N개의 정점이 있는 트리
트리 모든 리프 노드에 말이 있다.
부모 노드로 말을 옮김 루트 노드에 도착하면 말이 제거 됨
말이 없어 고를 수 없는 사람이 지게 된다

입력
트리의 정점 개수 N
간선 정보

출력
성원이가 이기면 yes 아니면 no

각 리프 노드의 깊이를 구한뒤, 리프 노드들의 깊이 합이 홀수면 승리 아님 패배
'''
import sys
sys.setrecursionlimit(1000000)

def solution(node):
    global ans
    
    # 리프노드 확인
    is_leaf = True 

    for next in arr[node]:
        if not distance[next]:                      
            distance[next] = distance[node]+1
            solution(next)
            is_leaf = False 
    
    # 리프 노드라면
    if is_leaf:                                     
        ans += distance[node] - 1

N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
distance = [0] * (N+1)
ans = 0

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

distance[1] = 1
solution(1)

# 답 출력
if ans % 2:
    print('Yes')
else:
    print('No')
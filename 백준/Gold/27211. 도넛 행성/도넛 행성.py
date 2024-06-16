'''
백준 27211 도넛 행성

N X M칸으로 이루어진 도넛 행성에 살고있다.
행성에는 격자 모양으로 줄이 그어져있다.
각 칸은 숲으로 막혀있거나 지나갈 수 있도록 비어있다.

집 기준 (0,0) 상하좌우로 이동 가능

행성 탐험하려 한다.
숲에 막히지 않은칸은 같은 구역으로 취급, 막혀있다면 다른구역이다.
빈 구역의 개수를 구하라


입력
N과 M
N개 줄에 걸쳐 칸 정보가 주어진다.
0이라면 비어있고, 1이면 숲으로 막혀있다.

출력
탐험할 수 있는 구역 개수

0이 있는 칸 bfs 실행
도넛 모양이기 때문에, 격자를 벗어나면 인덱스 재설정
'''
from collections import deque  

def bfs(i, j):
    q = deque()
    q.append((i,j))
    
    while q:
        si, sj = q.popleft()
        
        for d in range(4):
            ni = si + di[d]
            nj = sj + dj[d]
            
            # 행이 격자를 벗어나는 경우 인덱스 재설정
            if ni < 0:
                ni = N + ni
            elif ni >= N:
                ni = ni - N
            
            # 열이 격자를 벗어나는 경우 인덱스 재설정
            if nj < 0:
                nj = M + nj
            elif nj >= M:
                nj = nj - M
            
            # 큐에 추가, 방문처리
            if arr[ni][nj] == 0:
                q.append((ni, nj))
                arr[ni][nj] = 1

# 이동 방향
di = [1,-1,0,0]
dj = [0,0,1,-1]

# 행 열 크기 입력
N, M = map(int, input().split())
# 행성정보
arr = [[*map(int, input().split())] for _ in range(N)]
 
ans = 0  

# 모든 칸 순회
for i in range(N):
    for j in range(M):
        # 비어있는 칸이면 bfs실행 답 추가
        if arr[i][j] == 0:
            bfs(i, j)
            ans += 1

print(ans)



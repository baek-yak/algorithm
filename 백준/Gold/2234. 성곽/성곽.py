'''
2234 성곽
벽의 정보 서쪽 1(0001), 북쪽 2(0010), 동쪽 4(0100), 남쪽 8(1000) 벽이 있을 때 각 숫자를 더한 값이 주어짐(이진수 각 자리수 1)
&로 필터링

출력
1. 성에 있는 방의 갯수
- bfs를 사용한 횟수가 방의 개수
2. 가장 넓은 방
- bfs의 최댓값
3. 벽을 하나 제거할 떼 가장 넓은 방
- 인접한 방의 넓이
'''
from collections import deque

# bfs 함수 정의
def bfs(i, j):
    q = deque()
    q.append([i, j])
    visit[i][j] = 1
    room = 1
    
    while q:
        i, j = q.popleft()
        wall = 1
        
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            
            if ((arr[i][j] & wall) != wall): 
                if 0 <= ni < M and 0 <= nj < N and not visit[ni][nj]:
                    room += 1
                    visit[ni][nj] = 1
                    q.append([ni, nj])
            wall = wall*2
    return room

# 4방향
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

# 높이, 너비
N, M = map(int, input().split())
# 성벽 정보
arr = [list(map(int, input().split())) for _ in range(M)]
# 방문 체크
visit = [[0] * N for _ in range(M)]

# bfs 횟수
cnt = 0
# 최대 넓이 방
max_room = 0
# 벽 제거 최대 넓은 방
p_room = 0

for i in range(M):
    for j in range(N):
        if visit[i][j] == 0:
            cnt += 1
            max_room = max(max_room, bfs(i, j))

for i in range(M):
    for j in range(N):
        num = 1
        while num < 9:
            if num & arr[i][j]:
                visit = [[0] * N for _ in range(M)]
                arr[i][j] -= num
                p_room = max(p_room, bfs(i, j))
                arr[i][j] += num
            num *= 2
            
print(cnt)
print(max_room)
print(p_room)
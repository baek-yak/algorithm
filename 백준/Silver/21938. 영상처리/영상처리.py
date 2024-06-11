'''
백준 21938 영상처리

세로 길이가 N, 가로 길이가 M인 화면은 N * M개의 픽셀로 구성되어 있다.
(i, j)에 있는 픽셀은 RGB 색상의 의미를 담고 있다. 각 색상은 0 <= <=255로 표현 가능하다.
모든 픽셀에서 세 가지 색상을 평균내어 경계값 T 보다 크거나 같으면 255, 작으면 0으로 바꿔 새로운 화면으로 저장한다.
값이 255인 픽셀은 물체로 인식한다. 값이 255인 픽셀이 인접해 있다면 같은 물체로 인식한다
총 몇개의 물체가 있는지 구해라 

입력
세로 N, 가로 M
i번째 가로를 구성하고 있는 픽셀의 RGB 값이 M개가 N줄 입력
경계값 T

출력
물체의 개수, 없다면 0 출력

처음에 값을 받을때부터 계산해서 풀이
한 픽셀을 구성하는 것은 3개로 고정적이므로 열을 기준으로 3개씩 짤라주며 합을 저장
계산 편하게 하기 위해 T*3
방문을 안하고, 경계값을 넘는 위치에서 bfs를해 인접 픽셀 구하고, 개수를 증가
'''
from collections import deque

# 너비 우선 탐색
def bfs(i, j):
    q = deque()
    # 시작점 큐에 추가
    q.append((i, j))

    # 시작점 방문 표시
    visited[i][j] = 0

    while q:
        # 현재 위치
        i, j = q.popleft()

        # 4방향 탐색
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # 범위 내 확인
            if 0 <= ni < N and 0 <= nj < M:
                # 방문하지 않고, T 이상인 경우
                if visited[ni][nj] and arr[ni][nj] >= T:
                    # 방문 표시
                    visited[ni][nj] = 0
                    # 큐에 추가
                    q.append((ni, nj))

# 가로, 세로 입력
N, M = map(int, input().split())

arr = []

# 각 픽셀의 RGB 합해여 저장
for i in range(N):
    x = list(map(int, input().split()))
    temp = []
    for j in range(M):
        temp.append(sum(x[j*3:(j+1)*3]))
    
    arr.append(temp)

# 경계 값 입력 후 RGB 합산 기준으로 변경
T = int(input())
T = T * 3

# 방문 여브 체크 리스트
visited = [[1 for _ in range(M)] for _ in range(N)]
    
# 4방향
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

ans = 0

# 전체 탐색
for i in range(N):
    for j in range(M):
        # T 이상이고, 방문하지 않은 경우 bfs 탐색후 물체 증가
        if arr[i][j] >= T and visited[i][j]:
            bfs(i, j)
            ans += 1

print(ans)
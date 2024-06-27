'''
백준 2573 빙산

지구 온난화로 빙산이 녹고있다.
빙산을 2차원 배열에 표시
빙산의 각 부분별 높이 정보는 배역의 각칸에 양의 정수로 저장된다.
빙산의 높이는 바닷물에 접해있는 부분의 수 만큼 줄어든다.
빙산이 주어질 때, 빙산이 두 덩이리 이상으로 분리되는 최소 시간을 구하는 프로그램을 작성

입력
행의 개수 N, 열의 개수 M
N개의 줄에 M개의 정수
배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다

출력
빙산이 분리되는 최소의 시간

bfs로 풀이
'''
from collections import deque

def bfs(si, sj, v):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0),(1, 0),(0, -1),(0, 1)):
            ni = ci + di
            nj = cj + dj
            if v[ni][nj] == 0 and arr[ni][nj] > 0:
                q.append((ni, nj))
                v[ni][nj] = 1

# 년
def solve(): 
    for year in range(1, 900000):
        # 0의 개수 카운트
        a_sub = [[0]*M for _ in range(N)]
        for i in range(1, N-1):
            for j in range(1, M-1):
                if arr[i][j] == 0:
                    continue
                for di, dj in ((-1, 0),(1, 0),(0, -1),(0, 1)):
                    ni = i + di
                    nj = j + dj
                    if arr[ni][nj] == 0:
                        a_sub[i][j] += 1

        # 빙산 높이 낮추기
        for i in range(1, N-1):
            for j in range(1, M-1):
                if a_sub[i][j] > 0:
                    arr[i][j] = max(0, arr[i][j] - a_sub[i][j])

        # 덩어리 개수 카운트
        v = [[0]*M for _ in range(N)]
        cnt = 0
        for i in range(1, N-1):
            for j in range(1, M-1):
                if v[i][j] == 0 and arr[i][j] > 0:
                    bfs(i, j, v)
                    cnt += 1
                    # 두 덩어리
                    if cnt > 1: 
                        return year
        if cnt == 0:  
            return 0

# 인풋
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = solve()
print(ans)
'''
백준 1012 유기농 배추

지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호
어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 
이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
그 배추들 역시 해충으로부터 보호받을 수 있다. 
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것

입력
테스트 케이스
배추밭 가로길이 세로길이 배추위치 개수
배추 위치 xy

출력
필요한 최소 지렁이 수

bfs로 문제 풀이
'''
from collections import deque
# 테스트 케이스
t = int(input()) 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# bfs 함수
def bfs(arr, x, y): 
    q = deque()
    q.append([x, y])
    # 방문 처리
    arr[x][y] = 0 
    
    while q: 
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위내, 미방문
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1: 
                q.append([nx, ny])
                arr[nx][ny] = 0


for _ in range(t):  
    m, n, k = map(int, input().split())
    
    # 빈 배추밭
    arr = [[0]*(n) for _ in range(m)] 
    # 배추 위치 표기
    for _ in range(k):
        i, j = map(int, input().split())
        arr[i][j] = 1 
    
    ans = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(arr, i, j)
                # bfs 함수 들어갈때마다 + 1
                ans += 1 
    print(ans)
'''
백준 11403 경로 찾기

가중치 없는 방향그래프가 주어질때, 모든 정점에 대해 i에서 j로 가는 길이가 양수인 경로 유뮤를 구하라

입력
정점의 개수 N
N개의 줄에 그래프 인접 행렬
1인경우 간선 존재 0인 경우 경로 없음

출력
N개 줄에 걸쳐 인접행렬 형식으로 출력

dfs로 풀이
'''
def dfs(x):
    for i in range(n):
        # 현재 노드에서 i로의 경로가 존재하고, i 아직 방문 전이라면 방문처리 재귀호출
        if arr[x][i] == 1 and v[i] == 0:
            v[i] = 1
            dfs(i)

# 인풋
n = int(input())
# 그래프
arr = [list(map(int, input().split())) for _ in range(n)]
# 방문처리
v = [0 for _ in range(n)]

# 정점에 대해 dfs
for i in range(n):
    dfs(i)
    for j in range(n):
        if v[j] == 1:
            print(1, end=' ')
        else :
            print(0, end=' ')
    print()
    # 방문 처리 초기화
    v = [0 for _ in range(n)]
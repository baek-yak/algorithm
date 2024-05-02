'''
14621 나만 안되는 연애

사심경로 조건
1 이성으로 연결됨
2. 모든 대학교로 이동 가능
3. 최단 거리여야 한다.

입력
n 학교 수, m 도로 수

출력
도로의 길이 출력(경로가 안만들어지면 -1)

크루스칼 알고리즘
'''
# 부모 노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 집합 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 학교 수, 도로 수
n, m = map(int, input().split())
# 학교 성별
gender = list(input().split())
# 부모노드
parent = [i for i in range(n + 1)]

# 답
ans = 0
# 연결 도로 확인 변수
path = 0

# 간선 저장
edges = []
for i in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

# 거리 순 정렬
edges.sort()


for i in edges:
    d, u, v = i
    # 두 학교가 같은 집합이 아니고, 성별이 다르면 합침
    if find(u) != find(v) and gender[u-1] != gender[v-1]:
        union(u, v)
        ans += d
        path += 1

# 답 출력
if path == n - 1:
    print(ans)
else:
    print(-1)
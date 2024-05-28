'''
백준 1326 폴짝 폴짝

개구리가 징검다리를 건넌다.
징검다리에 숫자가 있는데 개구리는 징검다리에 쓰여 있는 수의 배수 만큼 떨어져 있는 곳으로 이동
a번째에서 b 징검다리로 이동할때 최소 몇 번 점프해야하는가

입력
징검다리 N
n의 정수
a,b

출력
최소 점프 횟수 갈수 없는 경우 -1
'''
from collections import deque

def bfs(a, b, n, arr):
    q = deque([a - 1])
    visited[a - 1] = 0

    while q:
        ci = q.popleft()

        for i in range(ci, n, arr[ci]):
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[ci] + 1

                if i == b - 1:
                    return visited[i]
                
        for i in range(ci, -1, -arr[ci]):
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[ci] + 1
                
                if i == b - 1:
                    return visited[i]
                
    return -1

n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
visited = [-1] * n

ans = bfs(a, b, n, arr)

print(ans)
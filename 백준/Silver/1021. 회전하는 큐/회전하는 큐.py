'''
백준 1021 회전하는 큐

N개의 원소를 포함하고 있는 양방향 순환 큐
큐에서 원소를 뽑으려 한다

아래 3가지 연산 수행 가능
1. 첫 번째 원소를 뽑는다.
2. 왼쪽으로 한 칸 이동
3. 오른쪽으로 한 칸 이동

큐에 있는 N이 주어지고, 뽑아야하는 원소의 위치가 주어진다
이때 원소를 뽑아는데 드는 2, 3번 연산의 최솟값을 출력하는 프로그램 작성

입력
큐의 크기 N, 뽑아내려고 하는 수의 개수 M
지민이가 뽑아내려고 하는 수의 위치

출력
정답 출력

뽑아내려고 하는 숫자를 차례로 꺼내서 큐의 첫번째 원소가 될때까지 왼쪽 or 오른쪽으로 이동
index <= len//2 만족하면 왼쪽이동 아니면 오른쪽이동해서 최솟화.
'''
from collections import deque

# 입력
N, M = map(int, input().split())

# 1부터 N까지 숫자로 이뤄진 큐 생성
arr = deque([i for i in range(1, N+1)])

# 뽑는 수 위치 입력
index = list(map(int, input().split()))

ans = 0

for i in index:
    while True:
        # 뽑는 숫자가 큐의 첫 번째 원소인 경우, 뽑고 탈출
        if arr[0] == i:
            arr.popleft()
            break
        else:
            # 뽑는 숫자가 앞쪽에 가까운경우, 왼쪽으로 이동
            if arr.index(i) <= len(arr)//2:
                arr.rotate(-1)
                ans += 1
            # 뽑는 숫자가 뒤쪽에 가까운경우, 오른쪽으로 이동
            else:
                arr.rotate(1)
                ans += 1

print(ans)
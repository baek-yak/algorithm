'''
17276 배열 돌리기
n * n 2차원 정수 배열 X 존재
X를 45도의 배수 만큼 시계 방향 or 반시계 방향으로 돌린다.
1. x의 주 대각선(i,i)을 가운데 열로 옮긴다
2. x의 가운데 열을 x의 부 대각선으로 옮긴다
3. x의 부 대각선을 x의 가운데 행으로 옮긴다
4. x의 가운데 행을 주 대각선으로 옮긴다

위 네 가지 경우 모두 원소의 순서는 유지 되어야 하고, 다른 원소의 위치는 변하지 않는다.
'''
import sys
input = sys.stdin.readline

ans = []
# 데이터 받기
case = int(input())

for _ in range(case):
    n, d = map(int, input().split())
    
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    # 각도가 음수이면 양수로 바꾸기
    if d < 0 :
        d = 360 + d
    
    start = (d // 45) - 1
    
    # 회전 전
    before = []
    # 주 대각선
    before.append([arr[i][i] for i in range(n)])
    # 가운데 열
    before.append([arr[i][(n+1)//2 -1] for i in range(n)])
    # 부 대각선
    before.append([arr[n-i-1][i] for i in range(n-1, -1, -1)])
    # 가운데 행
    before.append([arr[(n+1)//2-1][i] for i in range(n-1, -1, -1)])
    
    # 회전 후
    after = [[0]*n for _ in range(n)]
    
    # 회전
    for r in range(4):
        idx = (r + start) % 8
        
        if idx == 0 or idx == 4:
            if idx == 0:
                for i in range(n):
                    after[i][(n + 1) // 2 - 1] = before[r][i]
            else:
                for i in range(n):
                    after[n-i-1][(n + 1) // 2 - 1]  = before[r][i]
                    
        elif idx == 1 or idx == 5:
            if idx == 1:
                for i in range(n):
                    after[i][n-i-1] = before[r][i]
            else:
                for i in range(n):
                    after[n-i-1][i] = before[r][i]
        
        elif idx == 2 or idx == 6:
            if idx == 2:
                for i in range(n):
                    after[(n+1)//2 - 1][n-i-1] = before[r][i]
            else:
                for i in range(n):
                    after[(n+1)//2 - 1][i] = before[r][i]
        
        elif idx == 3 or idx == 7:
            if idx == 3:
                for i in range(n):
                    after[n-i-1][n-i-1] = before[r][i]
            else:
                for i in range(n):
                    after[i][i] = before[r][i]
    
    # 남은 칸 채우기
    for i in range(n):
        for j in range(n):
            if after[i][j] == 0:
                after[i][j] = arr[i][j]
    
    for i in range(n):
        ans.append(after[i])

for _ in range(len(ans)):
    print(*ans[_])